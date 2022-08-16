import re
import tensorflow as tf
import tensorflow_text as text
import pathlib
from tensorflow_text.python.ops.bert_tokenizer import BasicTokenizer
from tensorflow.python.ops import string_ops


reserved_tokens=["[PAD]", "[UNK]"]

ipt_bert_vocab_args = dict(
    # The target vocabulary size
    vocab_size = 10000,
    # Reserved tokens that must be included in the vocabulary
    reserved_tokens=reserved_tokens,
    # Arguments for `text.BertTokenizer`
    bert_tokenizer_params={},
    # Arguments for `wordpiece_vocab.wordpiece_tokenizer_learner_lib.learn`
    learn_params={},
)

opt_bert_vocab_args = dict(
    # The target vocabulary size
    vocab_size = 16384,
    # Reserved tokens that must be included in the vocabulary
    reserved_tokens=reserved_tokens,
    # Arguments for `text.BertTokenizer`
    bert_tokenizer_params={},
    # Arguments for `wordpiece_vocab.wordpiece_tokenizer_learner_lib.learn`
    learn_params={},
)


def cleanup_text(reserved_tokens, token_txt):
    # Drop the reserved tokens, except for "[UNK]".
    bad_tokens = [re.escape(tok) for tok in reserved_tokens if tok != "[UNK]"]
    bad_token_re = "|".join(bad_tokens)

    bad_cells = tf.strings.regex_full_match(token_txt, bad_token_re)
    result = tf.ragged.boolean_mask(token_txt, ~bad_cells)

    # Join them into strings.
    result = tf.strings.reduce_join(result, separator=' ', axis=-1)

    return result


class InputBasicTokenizer(BasicTokenizer):
    def lower_case(self, text_input):
        """Lower-cases the `text_input'."""
        text_input = tf.strings.lower(text_input, encoding='utf-8', name=None)
        text_input = string_ops.regex_replace(text_input, r"\p{Mn}", "")
        return text_input


class OutputBasicTokenizer(BasicTokenizer):
    def lower_case(self, text_input):
        """Lower-cases the `text_input'."""
        text_input = tf.strings.lower(text_input, encoding='utf-8', name=None)
        return text_input


class CustomTokenizer(tf.Module):
    def __init__(self, reserved_tokens, vocab_path, is_ipt=False, lower_case_status=False, normalization_form=None):
        if is_ipt:
            self.tokenizer = text.BertTokenizer(vocab_path, lower_case=lower_case_status,
                                                normalization_form=normalization_form,
                                                basic_tokenizer_class=InputBasicTokenizer)
        else:
            self.tokenizer = text.BertTokenizer(vocab_path, lower_case=lower_case_status,
                                                normalization_form=normalization_form,
                                                basic_tokenizer_class=OutputBasicTokenizer)
        self._reserved_tokens = reserved_tokens
        self._vocab_path = tf.saved_model.Asset(vocab_path)

        vocab = pathlib.Path(vocab_path).read_text().splitlines()
        self.vocab = tf.Variable(vocab)

        # Include a tokenize signature for a batch of strings.
        self.tokenize.get_concrete_function(
            tf.TensorSpec(shape=[None], dtype=tf.string))

        # Include `detokenize` and `lookup` signatures for:
        #   * `Tensors` with shapes [tokens] and [batch, tokens]
        #   * `RaggedTensors` with shape [batch, tokens]
        self.detokenize.get_concrete_function(
            tf.TensorSpec(shape=[None, None], dtype=tf.int64))
        self.detokenize.get_concrete_function(
              tf.RaggedTensorSpec(shape=[None, None], dtype=tf.int64))

        self.lookup.get_concrete_function(
            tf.TensorSpec(shape=[None, None], dtype=tf.int64))
        self.lookup.get_concrete_function(
              tf.RaggedTensorSpec(shape=[None, None], dtype=tf.int64))

        # These `get_*` methods take no arguments
        self.get_vocab_size.get_concrete_function()
        self.get_vocab_path.get_concrete_function()
        self.get_reserved_tokens.get_concrete_function()

    @tf.function
    def tokenize(self, strings):
        enc = self.tokenizer.tokenize(strings)
        # Merge the `word` and `word-piece` axes.
        enc = enc.merge_dims(-2,-1)
        # enc = add_start_end(enc)
        return enc

    @tf.function
    def detokenize(self, tokenized):
        words = self.tokenizer.detokenize(tokenized)
        return cleanup_text(self._reserved_tokens, words)

    @tf.function
    def lookup(self, token_ids):
        return tf.gather(self.vocab, token_ids)

    @tf.function
    def get_vocab_size(self):
        return tf.shape(self.vocab)[0]

    @tf.function
    def get_vocab_path(self):
        return self._vocab_path

    @tf.function
    def get_reserved_tokens(self):
        return tf.constant(self._reserved_tokens)


tokenizers = tf.Module()

ipt_v = "vocab/ipt_vocab.txt"
opt_v = "vocab/opt_vocab.txt"
tokenizers.ipt = CustomTokenizer(reserved_tokens, ipt_v, is_ipt=True, lower_case_status=True)
tokenizers.opt = CustomTokenizer(reserved_tokens, opt_v, lower_case_status=True)

tokenizer_ipt = tokenizers.ipt
tokenizer_opt = tokenizers.opt

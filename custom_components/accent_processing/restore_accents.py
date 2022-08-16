import tensorflow as tf
import nltk
import os
from tokenizers import tokenizer_ipt, tokenizer_opt
from models import Transformer

import logging
nltk.download('punkt')

num_layers = 3
d_model = 256
dff = 1024
num_heads = 4

input_vocab_size = tokenizer_ipt.get_vocab_size().numpy()
target_vocab_size = tokenizer_opt.get_vocab_size().numpy()
dropout_rate = 0.1
learning_rate = 0.001
MAX_LENGTH = 40

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class DiacriticsRestorer():
    def __init__(self, checkpoint_path):
        self.transformer = Transformer(num_layers, d_model, num_heads, dff, input_vocab_size, target_vocab_size,
                                  pe_input=input_vocab_size, rate=dropout_rate)

        ckpt = tf.train.Checkpoint(transformer=self.transformer)

        ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

        # if a checkpoint exists, restore the latest checkpoint.
        if ckpt_manager.latest_checkpoint:
            logging.debug("checkpoint loaded: " + ckpt_manager.latest_checkpoint)
            ckpt.restore(ckpt_manager.latest_checkpoint)

    def add_diacritics(self, inp_sentence):
        logging.debug("\t\t--> TOKENIZED: ", tokenizer_ipt.detokenize(tokenizer_ipt.tokenize([inp_sentence]).numpy()))

        length = len(nltk.word_tokenize(inp_sentence))
        inp_sentence = tokenizer_ipt.tokenize([inp_sentence]).to_tensor(shape=[1, MAX_LENGTH])[0]
        decoder_input = tf.expand_dims(inp_sentence, 0)
        predictions = self.transformer(decoder_input, training=False)
        predicted_ids = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

        result = tf.squeeze(predicted_ids, axis=0).numpy()

        seq = [i for i in result if i < tokenizer_opt.get_vocab_size()]

        # for i, t in zip(decoder_input[0], result):
        #     print('{} ---> {} \t\t\t\t {} ----> {}\t({})'.format(i, tokenizer_ipt.detokenize([[i]]).numpy(), t,
        #                                                          tokenizer_opt.detokenize([[t]]).numpy(),
        #                                                          tokenizer_opt.detokenize([[t]]).numpy()[0].decode(
        #                                                              'utf8')))
        predicted_sentence = tokenizer_opt.detokenize([seq]).numpy()[0].decode('utf8')
        predicted_sentence = " ".join(predicted_sentence.split()[:length])

        return predicted_sentence


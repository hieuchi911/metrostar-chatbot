from underthesea import word_tokenize

# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from typing import Text, List
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.shared.nlu.training_data.message import Message

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('custom_components/UndertheseaTokenizer.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Rasa 3.x
# @DefaultV1Recipe.register(
#     DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER, is_trainable=False
# )
class UndertheseaTokenizer(Tokenizer):
    """Underthesea derived class from Tokenizer class"""

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        """Tokenizes the text of the provided attribute of the incoming message."""
        text = message.get(attribute)
        words = word_tokenize(text)
        logger.debug(f'Output of tokenizer: {words}')

        # return self._apply_token_pattern(words)

        tokens = self._convert_words_to_tokens(words, text)
        logger.debug(f'Output of ._convert_words_to_tokens(): {tokens}')

        # return tokens

        wtf_is_this = self._apply_token_pattern(tokens)
        logger.debug(f'Output of ._apply_token_pattern(): {wtf_is_this}')
        return wtf_is_this
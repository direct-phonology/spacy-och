from importlib.resources import files
from typing import Callable

from spacy.lang.zh import ChineseTokenizer, Segmenter
from spacy.language import Language
from spacy.util import load_config_from_str, registry

from .lex_attrs import LEX_ATTRS
from .stop_words import STOP_WORDS

DEFAULT_CONFIG = """
    [nlp]

    [nlp.tokenizer]
    @tokenizers = "spacy.och.OldChineseTokenizer"
"""

# For now, just extend the default Chinese tokenizer
class OldChineseTokenizer(ChineseTokenizer):
    pass


# Without a model, just segment by character
# https://spacy.io/api/tokenizer
@registry.tokenizers("spacy.och.OldChineseTokenizer")
def create_old_chinese_tokenizer() -> Callable[[Language], OldChineseTokenizer]:
    def old_chinese_tokenizer_factory(nlp: Language) -> OldChineseTokenizer:
        return OldChineseTokenizer(nlp.vocab, segmenter=Segmenter.char)

    return old_chinese_tokenizer_factory


# Add lookups to the registry
# https://spacy.io/api/lookups
@registry.lookups("och")
def register_lookups():
    return {file.stem[4:]: file for file in files("och.lookups").glob("*.json")}


# https://spacy.io/api/language#defaults
class OldChineseDefaults(Language.Defaults):
    config = load_config_from_str(DEFAULT_CONFIG)
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": False}


# https://spacy.io/api/language#class-attributes
@registry.languages("och")
class OldChinese(Language):
    lang = "och"
    Defaults = OldChineseDefaults


__all__ = ["OldChinese"]

from importlib.resources import files, read_text
from typing import Callable

from spacy.lang.zh import ChineseTokenizer, Segmenter
from spacy.language import Language
from spacy.util import load_config_from_str, registry

from .lex_attrs import LEX_ATTRS
from .stop_words import STOP_WORDS


# For now, just extend the default Chinese tokenizer
class OldChineseTokenizer(ChineseTokenizer):
    pass


# Without a model, just segment by character
# https://spacy.io/api/tokenizer
@registry.tokenizers("spacy_och.OldChineseTokenizer")
def create_old_chinese_tokenizer() -> Callable[[Language], OldChineseTokenizer]:
    def old_chinese_tokenizer_factory(nlp: Language) -> OldChineseTokenizer:
        return OldChineseTokenizer(nlp.vocab, segmenter=Segmenter.char)

    return old_chinese_tokenizer_factory


# Add lookups to the registry
# https://spacy.io/api/lookups
@registry.lookups("och")
def find_lookups():
    return {
        file.stem[4:]: str(file) for file in files("spacy_och.lookups").glob("*.json")
    }


# https://spacy.io/api/language#defaults
class OldChineseDefaults(Language.Defaults):
    config = load_config_from_str(read_text(__name__, "config.cfg"))
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": False}


# https://spacy.io/api/language#class-attributes
@registry.languages("och")
class OldChinese(Language):
    lang = "och"
    Defaults = OldChineseDefaults


__all__ = ["OldChinese"]

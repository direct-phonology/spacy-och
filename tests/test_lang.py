"""Test the Old Chinese language object."""

from unittest import TestCase

import spacy


class TestLanguage(TestCase):
    def test_import(self) -> None:
        """language object should be able to be imported"""
        nlp = spacy.blank("och")
        self.assertEqual(nlp.lang, "och")

    def test_tokenize(self) -> None:
        """should tokenize by character without a model defined"""
        nlp = spacy.blank("och")
        tokens = [str(token) for token in nlp("北冥有魚，其名為鯤。")]
        self.assertEqual(tokens, ["北", "冥", "有", "魚", "，", "其", "名", "為", "鯤", "。"])

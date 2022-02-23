"""Test Old Chinese lookup data."""

from unittest import TestCase

import spacy
import srsly


class TestLookups(TestCase):
    def test_pinyin_lookup(self) -> None:
        """character pinyin data should be available"""
        py_lookup_path = spacy.registry.lookups.get("och")()["pinyin"]
        pinyin = srsly.read_json(py_lookup_path)
        self.assertEqual(pinyin["㐁"], ["tiàn"])

    def test_numbers_lookup(self) -> None:
        """character numeric data should be available"""
        var_lookup_path = spacy.registry.lookups.get("och")()["numbers"]
        numeric = srsly.read_json(var_lookup_path)
        self.assertEqual(numeric["七"], {"value": 7, "type": "primary"})

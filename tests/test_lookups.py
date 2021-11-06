"""Test Old Chinese lookup data."""

from unittest import TestCase

import spacy
import srsly


class TestLookups(TestCase):
    def test_pinyin_lookup(self) -> None:
        """character pinyin lookup data should be available"""
        py_lookup_path = spacy.registry.lookups.get("och")()["pinyin_lookup"]
        pinyin = srsly.read_json(py_lookup_path)
        self.assertEqual(pinyin["㐁"], ["tiàn"])

    def test_variants_lookup(self) -> None:
        """character variant lookup data should be available"""
        var_lookup_path = spacy.registry.lookups.get("och")()["variants_lookup"]
        variants = srsly.read_json(var_lookup_path)
        self.assertEqual(variants["䡵"]["simplified"], ["𫟦"])

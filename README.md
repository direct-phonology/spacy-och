# spacy-och
[![ci](https://github.com/direct-phonology/spacy-och/actions/workflows/ci.yml/badge.svg)](https://github.com/direct-phonology/spacy-och/actions/workflows/ci.yml)
[![pypi](https://img.shields.io/pypi/v/spacy-och.svg?style=flat)](https://pypi.org/project/spacy-och/)

the Old Chinese (`och`) language for the [spaCy NLP library](https://spacy.io/).

## installation
requires spacy v3.
```sh
$ pip install spacy-och
```

## usage
this package currently doesn't include trained models and is intended for basic NLP usage only, via `nlp.blank()`. it tokenizes texts by character and supports the `Token.like_num` and `Token.is_stop` attributes.
```python
>>> import spacy
>>> nlp = spacy.blank("och")
>>> from spacy_och.examples import sentences
>>> doc = nlp(sentences[0])
>>> doc.text
子曰：「上下无常，非為邪也。進退无恆，非離群也。君子進德脩業、欲及時也，故无咎。」
>>> [t for t in doc if t.is_stop] # all stop words
[曰, ：, 非, 也, 。, 非, 也, 。, 、, 欲, 及, 也, 故, 。]
```
more functionality is coming soon!

## developing
after cloning the repository:
```sh
$ pip install -e ".[dev]"
$ pre-commit install
```
## building
build a source archive and distribution for a release:
```sh
$ rm -rf dist/*
$ python -m build
```
publish the release on [test PyPI](https://test.pypi.org/) (useful for making sure everything worked):
```sh
$ python -m twine upload --repository testpypi dist/*
```
if everything looks ok, upload to the real PyPI:
```sh
$ python -m twine upload dist/*
```
## license
code is licensed under the [MIT license](LICENSE). some lookups data is derived from files licensed under the [unicode data files and software license](https://www.unicode.org/license.html).

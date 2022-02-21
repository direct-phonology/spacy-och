# spacy-och
[![ci](https://github.com/direct-phonology/spacy-och/actions/workflows/ci.yml/badge.svg)](https://github.com/direct-phonology/spacy-och/actions/workflows/ci.yml)
[![pypi](https://img.shields.io/pypi/v/spacy-och.svg?style=flat)](https://pypi.org/project/spacy-och/)

the Old Chinese (`och`) language for the [spaCy NLP library](https://spacy.io/).

## installation
requires spacy v3.
```sh
$ pip install spacy-och
```

## developing
after cloning the repository:
```sh
$ pip install -e ".[dev]"
$ pre-commit install
```

### license
code is licensed under the [MIT license](LICENSE). some data in `och/lookups` is derived from files licensed under the [unicode data files and software license](https://www.unicode.org/license.html).

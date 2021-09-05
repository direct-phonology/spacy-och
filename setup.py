"""Packaging settings for och-spacy."""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf8")

setup(
    name="och",
    version="0.1.0",
    description="Old Chinese language and models for spaCy NLP library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/direct-phonology/och-spacy",
    author="Nick Budak",
    author_email="nbudak@princeton.edu",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Utilities",
    ],
    keywords="old chinese, phonology, linguistics, nlp, spacy",
    packages=find_packages(),
    install_requires=["spacy>=3"],
    entry_points={
        "spacy_languages": ["och=och:OldChinese"],
    },
)

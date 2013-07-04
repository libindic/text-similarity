#!/usr/bin/env python

from setuptools import setup, find_packages

name = "textsimilarity"

setup(
    name=name,
    version="0.2.1",
    url="http://silpa.org.in/textsimilarity",
    license="LGPL-3.0",
    description="Compare text and get a match score",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This module will compare two text
    s for their similarity.
    Based on the similarity it will give a number
    between 0 and 1. 1 means both text are similary.
    0 means texts are completely different. A
    value in between 0 and 1 indicates how much they are similar.
    The algorithm uses an n-grams model and cosine similarity.
    """,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools', 'silpa_common'],
    zip_safe=False,
)

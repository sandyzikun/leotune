#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name = "leotune",
    version = "0.0.2",
    description = "A Simple Python-based CLI-tool throwing out lyrics of VOCALOID works, which is similar to \"fortune\"",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/sandyzikun/leotune.git",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ],
    packages = setuptools.find_packages(),
    entry_points = {
        "console_scripts": [
            "leotune=leotune:lyricsfortune",
            ]
        }
    )
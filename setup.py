#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "HowieHye"

from setuptools import (setup, find_packages)

setup(
    name="qqpusher",
    version="0.1.3",
    description="SDK for qqpusher",
    url='https://github.com/howiehye/qqpusher.git',
    long_description=open('README.md', encoding='utf-8').read(),
    platforms=["all"],
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"],
    install_requires=[
        'requests>=2.25.0',
    ],
    packages=find_packages()
)

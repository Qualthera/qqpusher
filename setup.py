#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Qualthera"

from setuptools import (setup, find_packages)

setup(
    name="qqpusher",
    version="0.1.5",
    description="SDK for qqpusher",
    author='Qualthera',
    author_email='qualthera@163.com',
    mainitainer='HowieHye',
    mainitainer_email='howiehye@163.com',
    url='https://github.com/Qualthera/qqpusher.git',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='umbox',
    version='0.1.0',
    description='An umka package manager (server)',
    long_description=readme,
    author='Marek Maškarinec',
    author_email='marek@mrms.cz',
    url='https://git.sr.ht/~mrms/umboxs',
    license=license,
    packages=find_packages()
)

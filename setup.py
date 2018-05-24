#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
script_version = '3.1'

ir = []
try:
    with open('requirements.txt') as f:
        for line in f:
            line = line.strip()
            if line:
                if line[0] != '#': # For comments
                ir.append(line)
except FileNotFoundError:
    print('requirmemts.txt could not be found, try downloading a new version.')

setup(
    name='setti',
    version=script_version,
    description='Simple Python Library for Communicating with Edit the Text.',
    author='Tikolu',
    author_email='tikolu43@gmail.com',
    url='https://github.com/Tikolu/SETTI',
    packages=find_packages(),
    install_requires=ir,
    keywords='bot library python3')

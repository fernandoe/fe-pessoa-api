# -*- coding:utf-8 -*-
import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'source'))

setup(
    name='fe-pessoa-server',
    version='0.1.0',
    description='',
    long_description=README,
    url='https://github.com/fernandoe/fe-pessoa-server',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='Fernando Espíndola',
    author_email='fer.esp@gmail.com',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

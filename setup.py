#!/usr/bin/env python3

import os
import sys

import colout2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

packages = ['colout2']

requires = ['argparse', 'pygments', 'babel']

setup(
    name='colout2',
    version='1.0.2',
    description='Color Up Arbitrary Command Output.',
    long_description=open('README.md').read(),
    author='Omer Katz',
    author_email='omer.drow@gmail.com',
    url='http://nojhan.github.com/colout/',
    packages=packages,
    package_data={'': ['README.md', 'LICENSE']},
    package_dir={'colout2': 'colout2'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    entry_points={
        'console_scripts': [
            'colout2 = colout2.__main__:main'
        ]
    },
    zip_safe=False,
)

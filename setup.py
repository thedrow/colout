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
    version='1.0',
    description='Color Up Arbitrary Command Output.',
    long_description=open('README.md').read(),
    author='nojhan',
    author_email='nojhan@nojhan.net',
    url='http://nojhan.github.com/colout2/',
    packages=packages,
    package_data={'': ['LICENSE']},
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

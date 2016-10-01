#!/usr/bin/env python3

import os
import sys

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
    version='1.0.3',
    description='Color Up Arbitrary Command Output.',
    long_description="See https://github.com/thedrow/colout2",
    author='Omer Katz',
    author_email='omer.drow@gmail.com',
    url='http://nojhan.github.com/colout/',
    packages=packages,
    package_dir={'colout2': 'colout2'},
    include_package_data=True,
    install_requires=requires,
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'colout2 = colout2.__main__:main'
        ]
    },
    zip_safe=False,
)

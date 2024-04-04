#!/usr/bin/env python

from distutils.core import setup

setup(
      name='posit_calyx_benchmarking',
      version='0.0.1',
      description='Scripts validation and plotting',
      author='Nimalan',
      author_email='m.nimalan@thoughtworks.com',
      url='https://github.com/dic-case-studies/calyx-posit-evaluation',
      packages=['validation_utils'],
      install_requires=[
            "simplejson",
            "seaborn",
            "scikit-image"
      ]
)
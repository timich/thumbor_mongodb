#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from distutils.core import setup
from thumbor_mongodb import __version__

setup(
    name = "thumbor_mongodb",
    packages = ["thumbor_mongodb"],
    version = __version__,
    description = "MongoDB loader for Thumbor (with GridFS)",
    author = "Michal Tinka",
    author_email = "michal.tinka@gmail.com",
    keywords = ["thumbor", "mongodb", "images", "gridfs"],
    license = 'MIT',
    url = 'https://github.com/timich/thumbor_mongodb',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_mongodb": "thumbor_mongodb"},
    install_requires=["thumbor","pymongo"],
    long_description = """\
Thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
This module provide support for MongoDB loader for images stored in GridFS.
Image data is addressed by its ObjectId('_id')
"""
)
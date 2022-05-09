#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2012-2016 California Institute of Technology.
# Copyright (c) 2016-2022 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/ppft/blob/master/LICENSE

import os
import sys
# drop support for older python
unsupported = None
if sys.version_info < (2, 7):
    unsupported = 'Versions of Python before 2.7 are not supported'
elif (3, 0) <= sys.version_info < (3, 7):
    unsupported = 'Versions of Python before 3.7 are not supported'
if unsupported:
    raise ValueError(unsupported)

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

# This is a hack to import a minimal package for the build process
builtins.__PPFT_SETUP__ = True
sys.path.append(os.path.abspath(os.path.curdir))
import ppft

# get version numbers, long_description, etc
AUTHOR = ppft.__author__
VERSION = ppft.__version__
LONG_DOC = ppft.__doc__ #FIXME: near-duplicate of README.md
#LICENSE = ppft.__license__ #FIXME: duplicate of LICENSE
AUTHOR_EMAIL = 'mmckerns@uqfoundation.org'

# check if setuptools is available
try:
    from setuptools import setup
    from setuptools.dist import Distribution
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    Distribution = object
    has_setuptools = False

# build the 'setup' call
setup_kwds = dict(
    name='ppft',
    version=VERSION,
    description='distributed and parallel python',
    long_description = LONG_DOC,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    maintainer = AUTHOR,
    maintainer_email = AUTHOR_EMAIL,
    license = '3-clause BSD',
    platforms = ['Linux', 'Windows', 'Mac'],
    url = 'https://github.com/uqfoundation/ppft',
    download_url = 'https://pypi.org/project/ppft/#files',
    python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: Implementation :: PyPy',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development'],
    packages = ['ppft', 'ppft.tests', 'ppft.server', 'pp', 'pp.server'],
    package_dir = {'ppft':'ppft', 'pp':'pp', 'ppft.server':'ppft/server', \
                   'ppft.tests':'examples', 'pp.server':'pp/server'},
    scripts = ['ppft/server/ppserver'],
)

# force python-, abi-, and platform-specific naming of bdist_wheel
class BinaryDistribution(Distribution):
    """Distribution which forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

# define dependencies
six_version = 'six>=1.7.3'
dill_version = 'dill>=0.3.4'
# add dependencies
depend = [six_version]
extras = {'dill': [dill_version]}
# update setup kwds
if has_setuptools:
    setup_kwds.update(
        zip_safe=False,
        # distclass=BinaryDistribution,
        install_requires=depend,
        extras_require=extras,
    )

# call setup
setup(**setup_kwds)

# if dependencies are missing, print a warning
try:
    import six
    #import dill
except ImportError:
    print("\n***********************************************************")
    print("WARNING: One of the following dependencies is unresolved:")
    print("    %s" % six_version)
    print("    %s (optional)" % dill_version)
    print("***********************************************************\n")


if __name__=='__main__':
    pass

# end of file

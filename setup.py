#!/usr/bin/env python
# Parallel Python setup script
# For the latest version of the Parallel Python
# software visit: http://www.parallelpython.com
"""
Standard build tool for python libraries.
"""

import os, os.path
import sys
# drop support for older python
unsupported = None
if sys.version_info < (2, 7):
    unsupported = 'Versions of Python before 2.7 are not supported'
elif (3, 0) <= sys.version_info < (3, 6):
    unsupported = 'Versions of Python before 3.6 are not supported'
if unsupported:
    raise ValueError(unsupported)

pyversion = sys.version_info[0]
pkgdir = 'pp' if pyversion == 2 else 'ppft'
_pkgdir = pkgdir # 'src'
_server = os.path.join('ppft', 'server')
# import shutil
# shutil.copytree(pkgdir, _pkgdir)

try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False

stable_version = '1.6.6.4'
target_version = '1.6.6.4'
is_release = stable_version == target_version
VERSION = stable_version if is_release else target_version + '.dev0'
# os.chdir(pkgdir)
# sys.path.insert(0, '.')
# from ppcommon import __version__ as VERSION
# sys.path.pop(0)
# if os.path.exists('ppcommon.pyc'): os.remove('ppcommon.pyc')
# os.chdir('..')


LONG_DESCRIPTION = \
"""-------------------------------------
ppft: distributed and parallel python
-------------------------------------

About Ppft
==========

``ppft`` is a fork of Parallel Python, and is developed as part of ``pathos``: https://github.com/uqfoundation/pathos

Parallel Python module (``pp``) provides an easy and efficient way to create parallel-enabled applications for SMP computers and clusters. ``pp`` module features cross-platform portability and dynamic load balancing. Thus application written with ``pp`` will parallelize efficiently even on heterogeneous and multi-platform clusters (including clusters running other application with variable CPU loads). Visit http://www.parallelpython.com for further information.

``ppft`` is part of ``pathos``, a python framework for heterogeneous computing.
``ppft`` is in active development, so any user feedback, bug reports, comments,
or suggestions are highly appreciated.  A list of issues is located at https://github.com/uqfoundation/ppft/issues, with a legacy list maintained at https://uqfoundation.github.io/project/pathos/query.

NOTE: ``ppft`` installs as ``pp``. If ``pp`` is installed, it should be uninstalled before ``ppft`` is installed -- otherwise, ``import pp`` will likely not find the ``ppft`` fork.


Major Changes:
==============

    - ``pip`` and ``setuptools`` support
    - support for python 3
    - enhanced serialization, using ``dill.source``


Current Release
===============

This documentation is for version ``ppft-1.6.6.4`` (a fork of ``pp-1.6.6``).

The latest released version of ``ppft`` is available from::

    https://pypi.org/project/ppft

``pp`` and ``ppft`` are distributed under a BSD-like license.


Development Version
===================

You can get the latest development version with all the shiny new features at::

    https://github.com/uqfoundation

If you have a new contribution, please submit a pull request.


Installation
============

``ppft`` is packaged to install from source, so you must
download the tarball, unzip, and run the installer::

    [download]
    $ tar -xvzf ppft-1.6.6.4.tgz
    $ cd ppft-1.6.6.4
    $ python setup.py build
    $ python setup.py install

You will be warned of any missing dependencies and/or settings
after you run the "build" step above.

Alternately, ``ppft`` can be installed with ``pip`` or ``easy_install``::

    $ pip install ppft

NOTE: ``ppft`` installs as ``pp``. If ``pp`` is installed, it should be uninstalled before ``ppft`` is installed -- otherwise, ``import pp`` will likely not find the ``ppft`` fork.


Requirements
============

``ppft`` requires::

    - ``python``, **version == 2.7** or **version >= 3.6**, or ``pypy``
    - ``six``, **version >= 1.7.3**

Optional requirements::

    - ``setuptools``, **version >= 0.6**
    - ``dill``, **version >= 0.3.4**


More Information
================

Probably the best way to get started is to look at the set of example scripts
in ``ppft.examples``. You can run the test suite with ``python -m ppft.tests``.
``ppft`` will create and execute jobs on local workers (automatically created
using ``python -u -m ppft``). Additionally, remote servers can be created with 
``ppserver`` (or ``python -m ppft.server``), and then jobs can be distributed
to remote workers. See ``--help`` for more details on how to configure a server.
Please feel free to submit a ticket on github, or ask a question on
stackoverflow (**@Mike McKerns**).  If you would like to share how you use
``ppft`` in your work, please send an email (to **mmckerns at uqfoundation dot org**).


Citation
========

If you use ``ppft`` to do research that leads to publication, we ask that you
acknowledge use of ``ppft`` by citing the following in your publication::

    M.M. McKerns, L. Strand, T. Sullivan, A. Fang, M.A.G. Aivazis,
    "Building a framework for predictive science", Proceedings of
    the 10th Python in Science Conference, 2011;
    http://arxiv.org/pdf/1202.1056

    Michael McKerns and Michael Aivazis,
    "pathos: a framework for heterogeneous computing", 2010- ;
    https://uqfoundation.github.io/project/pathos

Please see https://uqfoundation.github.io/project/pathos or
http://arxiv.org/pdf/1202.1056 for further information.

"""

kwds = {
        "name" : "ppft",
        "url" : "https://github.com/uqfoundation/ppft",
        "version" : VERSION,
        "download_url" : "https://github.com/uqfoundation/ppft/releases/download/ppft-%s/ppft-%s.tar.gz" % (stable_version, stable_version),
        "author" : "Mike McKerns",
        "maintainer" : "Mike McKerns",
        "packages" : ["ppft","pp","ppft.tests","ppft.server"],
        "package_dir" : {'ppft': _pkgdir,'pp': _pkgdir,'ppft.server': _server,'ppft.tests':'examples'},
        "scripts" : ["%s/ppserver" % _server],
        "description" : "distributed and parallel python",
        "platforms" : ["Windows", "Linux", "Mac"],
        "long_description" : LONG_DESCRIPTION,
        "license" : "BSD-like",
        "classifiers" : [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        ],
}

if has_setuptools:
    kwds.update({
        "zip_safe" : False,
        "extras_require" : {'dill': ['dill>=0.3.4']},
    })
if has_setuptools and pyversion > 2:
    kwds.update({
        "install_requires" : ['six>=1.7.3'],
    })

setup(**kwds)

# if os.path.exists(_pkgdir):
#     shutil.rmtree(_pkgdir)

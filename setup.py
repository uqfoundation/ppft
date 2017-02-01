#!/usr/bin/env python
# Parallel Python setup script
# For the latest version of the Parallel Python
# software visit: http://www.parallelpython.com
"""
Standard build tool for python libraries.
"""

import sys
import os, os.path
pyversion = sys.version_info[0]
pkgdir = 'python%s' % pyversion
_pkgdir = pkgdir # 'src'
# import shutil
# shutil.copytree(pkgdir, _pkgdir)

try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False

stable_version = '1.6.4.6'
target_version = '1.6.4.7'
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

ppft is a fork of Parallel Python, and is developed as part of pathos: https://github.com/uqfoundation/pathos

Parallel Python module (PP) provides an easy and efficient way to create parallel-enabled applications for SMP computers and clusters. PP module features cross-platform portability and dynamic load balancing. Thus application written with PP will parallelize efficiently even on heterogeneous and multi-platform clusters (including clusters running other application with variable CPU loads). Visit http://www.parallelpython.com for further information.

Pathos is a python framework for heterogeneous computing.
Pathos is in active development, so any user feedback, bug reports, comments,
or suggestions are highly appreciated.  A list of known issues is maintained
at http://trac.mystic.cacr.caltech.edu/project/pathos/query, with a public
ticket list at https://github.com/uqfoundation/pathos/issues.

NOTE: ppft installs as pp. If pp is installed, it should be uninstalled before ppft is installed -- otherwise, "import pp" will likely not find the ppft fork.


Major Changes:
==============

    - pip and setuptools support
    - support for python 3
    - enhanced serialization, using dill.source


Current Release
===============

This version is ppft-1.6.4.6 (a fork of pp-1.6.4).

The latest released pathos fork of PP is available from::

    https://pypi.python.org/pypi/ppft

PP is distributed under a BSD-like license.


Development Version
===================

You can get the latest development version with all the shiny new features at::

    https://github.com/uqfoundation

If you have a new contribution, please submit a pull request.


Installation
============

Ppft is packaged to install from source, so you must
download the tarball, unzip, and run the installer::

    [download]
    $ tar -xvzf ppft-1.6.4.6.tgz
    $ cd ppft-1.6.4.6
    $ python setup.py build
    $ python setup.py install

You will be warned of any missing dependencies and/or settings
after you run the "build" step above.

Alternately, ppft can be installed with pip or easy_install::

    $ pip install ppft

NOTE: ppft installs as pp. If pp is installed, it should be uninstalled before ppft is installed -- otherwise, "import pp" will likely not find the ppft fork.


Requirements
============

Ppft requires::

    - python2, version >= 2.5  *or*  python3, version >= 3.1
    - six, version >= 1.7.3

Optional requirements::

    - setuptools, version >= 0.6
    - dill, version >= 0.2.6


More Information
================

Probably the best way to get started is to look at the examples that are
provided within PP.  See pp.examples for a set of scripts.  Please feel
free to submit a ticket on github, or ask a question on stackoverflow
(@Mike McKerns).

Pathos is an active research tool. There are a growing number of publications
and presentations that discuss real-world examples and new features of pathos
in greater detail than presented in the user's guide.  If you would like to
share how you use pathos in your work, please post a link or send an email
(to mmckerns at uqfoundation dot org).


Citation
========

If you use pathos to do research that leads to publication, we ask that you
acknowledge use of pathos by citing the following in your publication::

    M.M. McKerns, L. Strand, T. Sullivan, A. Fang, M.A.G. Aivazis,
    "Building a framework for predictive science", Proceedings of
    the 10th Python in Science Conference, 2011;
    http://arxiv.org/pdf/1202.1056

    Michael McKerns and Michael Aivazis,
    "pathos: a framework for heterogeneous computing", 2010- ;
    http://trac.mystic.cacr.caltech.edu/project/pathos

Please see http://trac.mystic.cacr.caltech.edu/project/pathos or
http://arxiv.org/pdf/1202.1056 for further information.

"""

kwds = {
        "name" : "ppft",
        "url" : "https://github.com/uqfoundation",
        "version" : VERSION,
        "download_url" : "http://dev.danse.us/packages/",
        "author" : "Mike McKerns",
        "maintainer" : "Mike McKerns",
        "maintainer_email" : "mmckerns at uqfoundation dot org",
        "package_dir" : {'': _pkgdir},
        "py_modules" : ["ppft", "pp", "ppauto", "ppcommon", "pptransport", "ppworker"],
        "scripts" : ["%s/ppserver.py" % _pkgdir],
        "description" : "distributed and parallel python",
        "platforms" : ["Windows", "Linux", "Mac"],
        "long_description" : LONG_DESCRIPTION,
        "license" : "BSD-like",
        "classifiers" : [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        ],
}

if has_setuptools:
    kwds.update({
        "zip_safe" : False,
    })
if has_setuptools and pyversion > 2:
    kwds.update({
        "install_requires" : ['six>=1.7.3'],
    })

setup(**kwds)

# if os.path.exists(_pkgdir):
#     shutil.rmtree(_pkgdir)

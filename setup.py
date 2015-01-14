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

try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False

# os.chdir(pkgdir)
# sys.path.insert(0, '.')
# from ppcommon import __version__ as VERSION
VERSION = '1.6.4.5'
# sys.path.pop(0)
# if os.path.exists('ppcommon.pyc'): os.remove('ppcommon.pyc')
# os.chdir('..')


LONG_DESCRIPTION = """
Parallel Python module (PP) provides an easy and efficient way to create \
parallel-enabled applications for SMP computers and clusters. PP module \
features cross-platform portability and dynamic load balancing. Thus \
application written with PP will parallelize efficiently even on \
heterogeneous and multi-platform clusters (including clusters running other \
application with variable CPU loads). Visit http://www.parallelpython.com \
for further information.
"""


kwds = {
        "name" : "ppft",
        "url" : "http://www.parallelpython.com",
        "version" : VERSION,
        "download_url" : "http://dev.danse.us/packages/",
        "author" : "Vitalii Vanovschi",
        "author_email" : "support@parallelpython.com",
        "maintainer" : "Mike McKerns",
        "maintainer_email" : "mmckerns@caltech.edu",
        "package_dir" : {'': pkgdir},
        "py_modules" : ["pp", "ppauto", "ppcommon", "pptransport", "ppworker"],
        "scripts" : ["%s/ppserver.py" % pkgdir],
        "description" : "Parallel and distributed programming for Python",
        "platforms" : ["Windows", "Linux", "Unix"],
        "long_description" : LONG_DESCRIPTION,
        "license" : "BSD-like",
        "classifiers" : [
        "Topic :: Software Development",
        "Topic :: System :: Distributed Computing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
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


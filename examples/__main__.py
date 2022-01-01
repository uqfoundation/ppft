#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2018-2022 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/ppft/blob/master/LICENSE

from __future__ import print_function
import glob
import os
try:
    import pox
    python = pox.which_python(fullpath=False)
    if not python:
        python = 'python'
    elif not pox.which(python):
        python = pox.which_python(fullpath=False, version=True)
except ImportError:
    python = 'python'
import subprocess as sp
from sys import platform
shell = platform[:3] == 'win'

suite = os.path.dirname(__file__) or os.path.curdir
tests = glob.glob(suite + os.path.sep + '*.py')
tests = [f for f in tests if not os.path.basename(f).startswith('__')]


if __name__ == '__main__':

    for test in tests:
        p = sp.Popen([python, test], shell=shell).wait()
        if not p:
            print('.', end='')
    print('')


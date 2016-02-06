#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015-2016 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/dill/LICENSE
"""
ppft -- a friendly Parallel Python fork
"""

from pp import *
from pp import __version__, _USE_SUBPROCESS, \
               _Task, _Worker, _RWorker, _Statistics
import ppauto as auto
import ppcommon as common
import pptransport as transport
import ppworker as worker

# comment out the following if this is a release
#__version__ += '.dev0'

#'''
#__version__ = __version__.rsplit('.',1)
#__version__[-1] = str(int(__version__[-1])+1) + '.dev0'
#__version__ = ".".join(__version__)
#'''


# EOF

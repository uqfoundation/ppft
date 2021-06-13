#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015-2016 California Institute of Technology.
# Copyright (c) 2016-2021 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/ppft/blob/master/LICENSE
"""
ppft -- a friendly Parallel Python fork
"""

from ._pp import *
from ._pp import __version__, _USE_SUBPROCESS, \
                 _Task, _Worker, _RWorker, _Statistics
from . import auto
from . import common
from . import transport
from . import worker

copyright = """Copyright (c) 2015-2016 California Institute of Technology.
Copyright (c) 2016-2021 The Uncertainty Quantification Foundation."""
# comment out the following if this is a release
#__version__ += '.dev0'

#'''
#__version__ = __version__.rsplit('.',1)
#__version__[-1] = str(int(__version__[-1])+1) + '.dev0'
#__version__ = ".".join(__version__)
#'''


# EOF

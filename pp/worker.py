#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015-2016 California Institute of Technology.
# Copyright (c) 2016-2021 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/ppft/blob/master/LICENSE
"""
ppft worker: ppworker to communicate with ppserver
"""
import sys
if sys.version_info[0] == 2:
    from pp.__main__ import *
    from pp.__main__ import _WorkerProcess, __version__
else:
    from ppft.__main__ import *
    from ppft.__main__ import _WorkerProcess, __version__


if __name__ == "__main__":
        # add the directory with worker.py to the path
        sys.path.append(os.path.dirname(__file__))
        wp = _WorkerProcess()
        wp.run()


# EOF

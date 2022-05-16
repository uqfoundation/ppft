ppft
====
distributed and parallel python

About Ppft
----------
``ppft`` is a friendly fork of Parallel Python (``pp``). ``ppft`` extends Parallel Python to provide packaging and distribution with ``pip`` and ``setuptools``, support for python 3, and enhanced serialization using ``dill.source``. ``ppft`` uses Parallel Python to provide mechanisms for the parallel execution of python code on SMP (systems with multiple processors or cores) and clusters (computers connected via network).

Software written in python finds applications in a broad range of the categories including business logic, data analysis, and scientific calculations. This together with wide availability of SMP computers (multi-processor or multi-core) and clusters (computers connected via network) on the market create the demand in parallel execution of python code.

The most common way to write parallel applications for SMP computers is to use threads. However, the python interpreter uses the GIL (Global Interpreter Lock) for internal bookkeeping, where the GIL only allows one python byte-code instruction to execute at a time, even on an SMP computer. Parallel Python overcomes this limitation, and provides a simple way to write parallel python applications. Internally, processes and IPC (Inter Process Communications) are used to organize parallel computations. Parallel Python is written so that the details and complexity of IPC are handled internally, and the calling application just submits jobs and retrieves the results. Software written with Parallel Python works in parallel on many computers connected via a local network or the Internet. Cross-platform portability and dynamic load-balancing allows Parallel Python to parallelize computations efficiently even on heterogeneous and multi-platform clusters. Visit http://www.parallelpython.com for further information on Parallel Python.

``ppft`` is part of ``pathos``, a python framework for heterogeneous computing.
``ppft`` is in active development, so any user feedback, bug reports, comments,
or suggestions are highly appreciated.  A list of issues is located at https://github.com/uqfoundation/ppft/issues, with a legacy list maintained at https://uqfoundation.github.io/project/pathos/query.


Major Features
--------------
``ppft`` provides:

* parallel execution of python code on SMP and clusters
* easy-to-understand job-based parallelization
* automatic detection of the number of effective processors
* dynamic processor allocation (at runtime)
* low overhead for jobs with the same function (through transparent caching)
* dynamic load balancing (jobs are distributed at runtime)
* fault-tolerance (if a node fails, tasks are rescheduled on the others)
* auto-discovery of computational resources
* dynamic allocation of computational resources
* SHA based authentication for network connections
* enhanced serialization, using ``dill.source``


Current Release
[![Downloads](https://static.pepy.tech/personalized-badge/ppft?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads)](https://pepy.tech/project/ppft)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/ppft?color=blue&label=conda%20downloads)](https://anaconda.org/conda-forge/ppft)
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-get%20help-black.svg)](https://stackoverflow.com/questions/tagged/parallel-python)
---------------
The latest released version of ``ppft`` is available from:
    https://pypi.org/project/ppft

``ppft`` is distributed under a 3-clause BSD license, and is a fork of ``pp-1.6.6``.


Development Version
[![Support](https://img.shields.io/badge/support-the%20UQ%20Foundation-purple.svg?style=flat&colorA=grey&colorB=purple)](http://www.uqfoundation.org/pages/donate.html)
[![Documentation Status](https://readthedocs.org/projects/ppft/badge/?version=latest)](https://ppft.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/uqfoundation/ppft.svg?label=build&logo=travis&branch=master)](https://travis-ci.com/github/uqfoundation/ppft)
[![codecov](https://codecov.io/gh/uqfoundation/ppft/branch/master/graph/badge.svg)](https://codecov.io/gh/uqfoundation/ppft)
-------------------
You can get the latest development version with all the shiny new features at:
    https://github.com/uqfoundation

If you have a new contribution, please submit a pull request.


Installation
------------
``ppft`` can be installed with ``pip``::

    $ pip install ppft

To include enhanced serialization, using ``dill.source``, install::

    $ pip install ppft[dill]

If Parallel Python is already installed, it should be uninstalled before ``ppft`` is installed -- otherwise, ``import pp`` may point to the original and not to the ``ppft`` fork.


Requirements
------------
``ppft`` requires:

* ``python`` (or ``pypy``), **==2.7** or **>=3.7**
* ``setuptools``, **>=42**
* ``wheel``, **>=0.1**
* ``six``, **>=1.7.3**

Optional requirements:

* ``dill``, **>=0.3.4**


More Information
----------------
Probably the best way to get started is to look at the documentation at
http://ppft.rtfd.io. Also, you can see a set of example scripts in
``ppft.examples``. You can run the test suite with ``python -m ppft.tests``.
``ppft`` will create and execute jobs on local workers (automatically created
using ``python -u -m ppft``). Additionally, remote servers can be created with 
``ppserver`` (or ``python -m ppft.server``), and then jobs can be distributed
to remote workers. See ``--help`` for more details on how to configure a server.
Please feel free to submit a ticket on github, or ask a question on
stackoverflow (**@Mike McKerns**).  If you would like to share how you use
``ppft`` in your work, please send an email (to **mmckerns at uqfoundation dot org**).


Citation
--------
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


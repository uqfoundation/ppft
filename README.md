ppft
====
distributed and parallel python

About Ppft
----------
``ppft`` is a fork of Parallel Python, and is developed as part of ``pathos``: https://github.com/uqfoundation/pathos

Parallel Python module (``pp``) provides an easy and efficient way to create parallel-enabled applications for SMP computers and clusters. ``pp`` module features cross-platform portability and dynamic load balancing. Thus application written with ``pp`` will parallelize efficiently even on heterogeneous and multi-platform clusters (including clusters running other application with variable CPU loads). Visit http://www.parallelpython.com for further information.

``ppft`` is part of ``pathos``, a python framework for heterogeneous computing.
``ppft`` is in active development, so any user feedback, bug reports, comments,
or suggestions are highly appreciated.  A list of issues is located at https://github.com/uqfoundation/ppft/issues, with a legacy list maintained at https://uqfoundation.github.io/pathos-issues.html.

NOTE: ``ppft`` installs as ``pp``. If ``pp`` is installed, it should be uninstalled before ``ppft`` is installed -- otherwise, ``import pp`` may not find the ``ppft`` fork.


Major Changes
-------------
* ``pip`` and ``setuptools`` support
* support for python 3
* enhanced serialization, using ``dill.source``


Current Release
---------------
This version is a fork of ``pp-1.6.4``.

The latest released version of ``ppft`` is available from::
    https://pypi.org/project/ppft

``pp`` and ``ppft`` are distributed under a BSD-like license.


Development Version
[![Travis Build Status](https://img.shields.io/travis/uqfoundation/ppft.svg?label=build&logo=travis&branch=master)](https://travis-ci.org/uqfoundation/ppft)
[![codecov](https://codecov.io/gh/uqfoundation/ppft/branch/master/graph/badge.svg)](https://codecov.io/gh/uqfoundation/ppft)
[![Downloads](https://pepy.tech/badge/ppft)](https://pepy.tech/project/ppft)
-------------------
You can get the latest development version with all the shiny new features at::
    https://github.com/uqfoundation

If you have a new contribution, please submit a pull request.


More Information
----------------
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
--------
If you use ``ppft`` to do research that leads to publication, we ask that you
acknowledge use of ``ppft`` by citing the following in your publication::

    M.M. McKerns, L. Strand, T. Sullivan, A. Fang, M.A.G. Aivazis,
    "Building a framework for predictive science", Proceedings of
    the 10th Python in Science Conference, 2011;
    http://arxiv.org/pdf/1202.1056

    Michael McKerns and Michael Aivazis,
    "pathos: a framework for heterogeneous computing", 2010- ;
    https://uqfoundation.github.io/pathos.html

Please see https://uqfoundation.github.io/pathos.html or
http://arxiv.org/pdf/1202.1056 for further information.


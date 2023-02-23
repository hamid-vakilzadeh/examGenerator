========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/examGenerator/badge/?style=flat
    :target: https://examGenerator.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/hamid-vakilzadeh/examGenerator/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/hamid-vakilzadeh/examGenerator/actions

.. |version| image:: https://img.shields.io/pypi/v/examgenerator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/examgenerator

.. |wheel| image:: https://img.shields.io/pypi/wheel/examgenerator.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/examgenerator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/examgenerator.svg
    :alt: Supported versions
    :target: https://pypi.org/project/examgenerator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/examgenerator.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/examgenerator

.. |commits-since| image:: https://img.shields.io/github/commits-since/hamid-vakilzadeh/examGenerator/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hamid-vakilzadeh/examGenerator/compare/v0.0.0...main



.. end-badges

An interface tto for automated exam generation

* Free software: MIT license

Installation
============

::

    pip install examgenerator

You can also install the in-development version with::

    pip install https://github.com/hamid-vakilzadeh/examGenerator/archive/main.zip


Documentation
=============


https://examGenerator.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

=========================================================
python-uic920 - Standalone UIC 920-14 country definitions
=========================================================

:Author: Neil Albrock
:Version: 0.1.0

UIC 920-14 defines numeric country codes for use in international rail data exchange.
`python-uic920` is a self contained module that converts between these codes and the 
corresponding ISO-3166-1 alpha-2 code, allowing for quick cross-referencing.
UIC country names are also supplied for reference.

Installation
============

::

    $ pip install uic920
    

Usage
=====

::

    >>> from uic920 import countries
    >>>
    >>> countries.get(70)
    Country(name=u'United Kingdom of Great Britain and Northern Ireland', iso='GB', uic='70')
    >>> countries.get('es')
    Country(name=u'Spain', iso='ES', uic='71')
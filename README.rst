.. image:: https://img.shields.io/badge/stdlib--only-yes-green.svg
    :target: https://img.shields.io/badge/stdlib--only-yes-green.svg

.. image:: https://travis-ci.org/cjrh/arglog.svg?branch=master
    :target: https://travis-ci.org/cjrh/arglog

.. image:: https://coveralls.io/repos/github/cjrh/arglog/badge.svg?branch=master
    :target: https://coveralls.io/github/cjrh/arglog?branch=master

.. image:: https://img.shields.io/pypi/pyversions/arglog.svg
    :target: https://pypi.python.org/pypi/arglog

.. image:: https://img.shields.io/github/tag/cjrh/arglog.svg
    :target: https://img.shields.io/github/tag/cjrh/arglog.svg

.. image:: https://img.shields.io/badge/install-pip%20install%20arglog-ff69b4.svg
    :target: https://img.shields.io/badge/install-pip%20install%20arglog-ff69b4.svg


arglog
======

*Add logging options to argparse automatically*

Demo
----

.. code:: python

    # main.py
    import argparse
    import logging
    import arglog

    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        arglog.patch(parser)
        args = parser.parse_args()

This will trigger the same effect as running:

.. code:: python

    logging.basicConfig(level='<level name>')

However, you now also have a new CLI option for your program:

.. code:: bash

    $ python main.py --loglevel=WARNING

All of the logging levels are supported, ``INFO``, ``DEBUG`` and so on.

=================
 amortize-loans
=================

:Authors: snidarian, caerulescens
:Description: Graphing your debt.... Visually!


=========
 install
=========

+------------+--------------------------------------------+
| dependency | description                                |
+============+============================================+
| python_    | C based programming language               |
+------------+--------------------------------------------+
| poetry_    | python packaging and dependency management |
+------------+--------------------------------------------+

=======
 usage
=======

install::

    poetry install

test::

    poetry run pytest

coverage::

    poetry run coverage run -m pytest
    poetry run coverage report -m

run::

    poetry run python main.py <args>


.. _python: https://www.python.org/
.. _poetry: https://python-poetry.org/
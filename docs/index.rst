.. ukpostcodevalidator documentation master file, created by
   sphinx-quickstart on Sat Mar 25 05:23:30 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


ukpostcodevalidator's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This library validates the uk postal code based on the formating rules found on this article
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

Installation
------------
You can install `ukpostcodevalidator` using pip:

::

    pip install ukpostcodevalidator


Usage
-----
To validate the postal code for UK just invole the validate method on the Uk class as show below:

.. code-block:: python

    >>> from ukpostcodevalidator import validator
    >>> validator.Uk.validate("AA9A 9AA")

Running Tests
-------------
To run tests for the project run the following command while inside the root directory ukpostcodevalidator

::

    py.test tests.py

Api Documentation
-----------------

.. automodule:: ukpostcodevalidator.validator
    :members:
    :undoc-members:
    :show-inheritance:


.. automodule:: ukpostcodevalidator
    :members:
    :undoc-members:
    :show-inheritance:

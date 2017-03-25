
[![Documentation Status](https://readthedocs.org/projects/ukpostcodevalidator/badge/?version=latest)](http://ukpostcodevalidator.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/eddmash/ukpostcodevalidator.svg?branch=master)](https://travis-ci.org/eddmash/ukpostcodevalidator)

This library validates the uk postal code based on the formating rules found on this article
<https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting>

Documentation can be found here
<http://ukpostcodevalidator.readthedocs.io/en/latest/>

Installation
------------
You can install `ukpostcodevalidator` using pip: 

    pip install ukpostcodevalidator


Usage
-----
To validate the postal code for UK just invole the validate method on the Uk class as show below:
 
    >>> from ukpostcodevalidator import validator
    >>> validator.Uk.validate("AA9A 9AA")
    
Running Tests
-------------
To run tests for the project run the following command while inside the root directory ukpostcodevalidator

    py.test tests.py 
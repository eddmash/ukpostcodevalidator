[![Documentation Status](https://readthedocs.org/projects/ukpostcodevalidator/badge/?version=latest)](http://ukpostcodevalidator.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/eddmash/ukpostcodevalidator.svg?branch=master)](https://travis-ci.org/eddmash/ukpostcodevalidator)

`Documentation <http://ukpostcodevalidator.readthedocs.io/en/latest/>`_

Installation
------------
You can install `ukpostcodevalidator` using pip: 

    pip install ukpostcodevalidator


Usage
-----
To validate the postal code for UK just invole the validate method on the Uk class as show below:
 
    >>> from ukpostcodevalidator import validator
    >>> validator.Uk.validate("AA9A 9AA")
    

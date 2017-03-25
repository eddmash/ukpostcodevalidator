This library validates the uk postal code based on the formating rules found on this article
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

Installation
------------
You can install `ukpostcodevalidator` using pip: 

    pip install ukpostcodevalidator


Usage
-----
To validate the postal code for UK just invole the validate method on the Uk class as show below:
 
    >>> from ukpostcodevalidator import validator
    >>> validator.Uk.validate("AA9A 9AA")
    

python_phabricator
==================

A Conduit Based Python API for Phabricator

-  Aims to be python based, no dependency on `Arcanist`_
-  Module Based format for API Requests (Easy to extend)
-  Session Token is Cached and takes into account expiry time

How to Use
==========

Minimal configuration as follows

.. code:: python

    # The Certificate of your phabricator installation that can be found
    # under settings
    CERT = 'YOUR_CERTIFICATE_HERE'

    # The authorized user on behalf of which to make the call
    USER = 'USER_NAME'

    # The phabricator URL without the PHAB
    PHAB = 'PHABRICATOR_URL'

-  Copy ``settings_sample.py`` as ``settings.py``
-  Fill out the values
-  Your certificate can be found in the `settings`_ page of your
   phabricator installation
-  Looking to make this customizable during setup

.. code:: bash

	msk@msk-ubuntu ~/projects/python_phabricator (master●)$ python
	Python 2.7.5+ (default, Feb 27 2014, 19:37:08) 
	[GCC 4.8.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from phabricator.paste.query import QueryPaste
	>>> p = QueryPaste()
	>>> p.makeRequest()
	loading token from disk cache
	Paste Id: PHID-PSTE-klpolzpskydol4lofldl
	Paste Id: PHID-PSTE-wfankndvvhullmp2rwgj
	Paste Id: PHID-PSTE-epwflteivngjxxu7d3yb
	Paste Id: PHID-PSTE-wrnmkkythul4wzm5c7qd

.. _Arcanist: https://github.com/facebook/arcanist
.. _settings: https://secure.phabricator.com/settings/panel/conduit/

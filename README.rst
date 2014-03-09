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

.. _Arcanist: https://github.com/facebook/arcanist
.. _settings: https://secure.phabricator.com/settings/panel/conduit/
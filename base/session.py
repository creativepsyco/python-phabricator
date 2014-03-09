import hashlib
import json
import requests
import time

from config.settings import *

# Format parameters for conduit.connect
current_timestamp = int(time.time())
signature = hashlib.sha1(str(current_timestamp) + CERT).hexdigest()
connect_params = {
    'client': 'Python demo',
    'clientVersion': 0,
    'clientDescription': 'A script for demonstrating conduit',
    'user': USER,
    'host': PHAB,
    'authToken': current_timestamp,
    'authSignature': signature,
}

TOKEN_DATA_FILE = 'token_data.json'


def not_expired(data):
    if 'expiry' not in data.keys():
        return False
    else:
        expiry_timestamp = int(data['expiry'])
        is_expired = current_timestamp > expiry_timestamp
        return not is_expired


def get_token():
    # Check for a cached token
    try:
        json_data = open(TOKEN_DATA_FILE)
        data = json.load(json_data)
    except Exception, e:
        data = {}
        # raise e

    # TODO: Check if expired already
    if 'sessionKey' in data.keys() and not_expired(data):
        print "loading token from disk cache"
        return data
    else:
        req = requests.post('%s/api/conduit.connect' % PHAB, data={
            'params': json.dumps(connect_params),
            'output': 'json',
            '__conduit__': True,
        })

        # Parse out the response (error handling ommitted)
        print req.content
        result = json.loads(req.content)['result']
        conduit = {
            'sessionKey': result['sessionKey'],
            'connectionID': result['connectionID'],
            'expiry': current_timestamp + 24 * 60 * 60
        }

        print "Your Conduit sessionKey: ", conduit

        with open(TOKEN_DATA_FILE, 'w') as outfile:
            json.dump(conduit, outfile)

        return conduit

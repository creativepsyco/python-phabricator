import hashlib
import json
import requests
import time

from config.settings import *

# Format parameters for conduit.connect
token = int(time.time())
signature = hashlib.sha1(str(token) + CERT).hexdigest()
connect_params = {
    'client': 'Python demo',
    'clientVersion': 0,
    'clientDescription': 'A script for demonstrating conduit',
    'user': USER,
    'host': PHAB,
    'authToken': token,
    'authSignature': signature,
}

# Make the request to conduit.connect
req = requests.post('%s/api/conduit.connect' % PHAB, data={
    'params': json.dumps(connect_params),
    'output': 'json',
    '__conduit__': True,
})

# Parse out the response (error handling ommitted)
result = json.loads(req.content)['result']
conduit = {
    'sessionKey': result['sessionKey'],
    'connectionID': result['connectionID'],
}

print "Your Conduit sessionKey: ", conduit

# # Make the call to phid.lookup
# req = requests.post('%s/api/phid.lookup' % PHAB, data={
#     'params': json.dumps({
#         'names': ['D1'],
#         '__conduit__': conduit,
#     }),
#     'output': 'json',
# })
# result = json.loads(req.content)['result']
# print result
# print result['D1']['fullName']
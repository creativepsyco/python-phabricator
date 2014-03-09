import hashlib
import json
import requests
import time

from config.settings import *
import session

class APIRequest(object):

    """Abstract Base APIRequest"""
    def getData(self):
        """To be over-ridden for getting the `params` data """
        pass

    def getUrl(self):
        """To be over-ridden for getting the `url` data """
        pass

    def processResponse(self, response):
        """"To be over-ridden for processing response """
        print "response from server"

    def makeRequest(self):
        conduit = session.get_token()

        data = {
            '__conduit__': conduit,
        }
        data = dict(data)
        data.update(self.getData())

        req = requests.post('%s/api/%s' % (PHAB, self.getUrl()), data={
                            'params': json.dumps(data),
                            'output': 'json',
                            })

        # TODO: Error Support?
        result = json.loads(req.content)['result']
        self.processResponse(result)

if __name__== "__main__":
	APIRequest().makeRequest()

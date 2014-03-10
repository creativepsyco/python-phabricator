import json
import requests
import sys

from phabricator.config.settings import *
import session

CONDUIT_INTERFACES = 'interfaces.json'


class ConduitRequest(object):

    def __init__(self):
        self.args = []

    def getData(self):
        """To be over-ridden for getting the `params` data """
        try:
            json_data = open(CONDUIT_INTERFACES)
            data = json.load(json_data)
            data = data[self.getUrl()]['args']
        except Exception, e:
            print e
            data = {}
        return data

    def getUrl(self):
        """To be over-ridden for getting the `url` data """
        return self.args[0]

    def processResponse(self, response):
        """"To be over-ridden for processing response """
        print "response from server\n", len(response)

    def makeRequest(self, *args, **kwargs):
        conduit = session.get_token()
        self.args = args

        data = {
            '__conduit__': conduit,
        }
        data = dict(data)
        data.update(self.getData())
        print data

        req = requests.post('%s/api/%s' % (PHAB, self.getUrl()), data={
                            'params': json.dumps(data),
                            'output': 'json',
                            })

        result = json.loads(req.content)['result']
        self.processResponse(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print """
        Format of the command is conduit.py COMMAND
        """
    ConduitRequest().makeRequest(sys.argv[1])

from phabricator.base.APIRequest import *

class QueryPaste(APIRequest):

    def getData(self):
        params = {}
        return params

    def getUrl(self):
        return "paste.query"

    def processResponse(self, response):
    	for key in response.keys():
    		print "Paste Id: %s" % key 


if __name__ == "__main__":
    print "making a request"
    myquery = QueryPaste()
    myquery.makeRequest()

    
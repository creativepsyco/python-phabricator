from base.APIRequest import *

class QueryPaste(APIRequest):

    def getData(self):
        params = {}
        return params

    def getUrl(self):
        return "paste.query"

if __name__ == "__main__":
    print "making a request"
    myquery = QueryPaste()
    myquery.makeRequest()
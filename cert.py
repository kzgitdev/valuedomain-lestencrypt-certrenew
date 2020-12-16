import os, sys, subprocess, requests, json, pprint

class Certificate:
    version = 1.0
    file = './apikey.txt'
    apikey = None
    domain = None
    url = None
    headers = None
    records = None
    updatedRecords = None

    def __init__(self, domain):
        self.welcomeMessage()
        self.domain = domain
        self.setApiKey()
        self.buildUrl()
        self.buildHeaders()
        self.setRecords()

    def setApiKey(self):
        with open(self.file) as f:
            self.apikey = f.readline().replace('\n', '')

    def buildUrl(self):
        self.url = 'https://api.value-domain.com/v1/domains/{}/dns'.format(self.domain)

    def buildHeaders(self):
        self.headers = {'Authorization': 'Bearer {}'.format(self.apikey)}

    def getRequest(self):
        r = requests.get(self.url, headers=self.headers)
        self.records = r.json()['results']['records']
        return self.records

    def setRecords(self):
        return self.getRequest()

    def getRecords(self):
        return self.records

    def addRecords(self, value):
        params = self.parseRecords()

        if (type(value) == str):
            params.append(value)
            self.updatedRecords = '\n'.join(params)
            return

        if (type(value) == list):
            params.extend(value)
            self.updatedRecords = '\n'.join(params)
            return

    def putRequest(self):
        records = { 
            'ns_type': 'valuedomain1',
            'records': self.updatedRecords,
            "ttl": "60"
        }
        r = requests.put(self.url, headers=self.headers, json=records)
        print(r.status_code)
  
    def removeRecords(self, value):
        params = self.records.splitlines()
        if (type(value) == str):
            value = value.split('\n')

        for i in value:
            params = [param for param in params if '{}'.format(i) not in param]

        self.updatedRecords = '\n'.join(params)
        return self.updatedRecords

    # convert from type:str records variable to be type:list variable.
    def parseRecords(self):
        return self.records.splitlines()

    # convert from type:list variable to be a tyle:str records variable.
    def joinRecords(self, value):
        return '\n'.join(value)

    # dig command
    def commandDig(self, value = None):
        if (value == None):
            value = self.domain
        
        os.system('dig @ns1.value-domain.com {}'.format(value))
        return

    def welcomeMessage(self):
        message = 'Welcome ! \nThis is the tool of domain\'s record  to add, update, delete and edit \nfrom value-domain API server. version{}'.format(self.version)
        print(message) 

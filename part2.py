import json
import urllib2

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641",
}

req = urllib2.Request('http://challenge.code2040.org/api/reverse', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)

string = response.read()


string = string[::-1]
data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641",
    "string": string
}

req = urllib2.Request('http://challenge.code2040.org/api/reverse/validate', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)
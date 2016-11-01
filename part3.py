import json
import urllib2
import ast

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641"
}

req = urllib2.Request('http://challenge.code2040.org/api/haystack', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)

dict = response.read()

dict = ast.literal_eval(dict)

string = dict['needle']
array = dict['haystack']

for index, element in enumerate(array):
    if string == element:
        answer = index
        break

data = {
        "token": "2ec4ddafc4256ca132ff3f4522449641",
        "needle": index
}

req = urllib2.Request('http://challenge.code2040.org/api/haystack/validate', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)
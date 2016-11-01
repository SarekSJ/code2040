import json
import urllib2
import ast
import re

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641"
}

req = urllib2.Request('http://challenge.code2040.org/api/prefix', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)

dict = response.read()

dict = ast.literal_eval(dict)

string = dict['prefix']
array = dict['array']

p = re.compile(string + '.')

final = []

for index, element in enumerate(array):
    if p.match(element):
        continue
    else:
        final.append(element)
print final

data = {
        "token": "2ec4ddafc4256ca132ff3f4522449641",
        "array": final
}

req = urllib2.Request('http://challenge.code2040.org/api/prefix/validate', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)
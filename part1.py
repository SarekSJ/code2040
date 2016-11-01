import json
import urllib2

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641",
    "github": "https://github.com/SarekSJ/code2040"
}

req = urllib2.Request('http://challenge.code2040.org/api/register', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)


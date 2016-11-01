import json
import urllib2
import ast
import datetime
import iso8601

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641"
}

req = urllib2.Request('http://challenge.code2040.org/api/dating', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)

dict = response.read()

dict = ast.literal_eval(dict)

datestamp = dict['datestamp']
interval = dict['interval']

datestamp_dt = iso8601.parse_date(datestamp)

datestamp_inc = datestamp_dt+datetime.timedelta(seconds=interval)

datestamp_iso = str(datestamp_inc.year) + "-" + str(datestamp_inc.month) + "-"+ str(datestamp_inc.day) + "T" + str(datestamp_inc.hour) + ":"+ str(datestamp_inc.minute)+":"+str(datestamp_inc.second)+"Z"
# datestamp_iso = "{%:y-%:m-:%dT:%H:%M:%SZ}".format(datestamp_inc)

data = {
    "token": "2ec4ddafc4256ca132ff3f4522449641",
    "datestamp": datestamp_iso
}

req = urllib2.Request('http://challenge.code2040.org/api/dating/validate', data=json.dumps(data))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req)


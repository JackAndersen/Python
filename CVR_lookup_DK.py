# Copyright, Jack Andersen - Wisecloud.dk
# Coding: utf-8
import urllib2
import json
import contextlib
import collections

#cvr to search for
cvrnr = 25798376

#counters to allow more than 200 lookups per day.
#useragent cannont be 0 but anything else is OK!
user_agent = 1
count = 0

if count == 190:
    user_agent = user_agent + 1
    count = 0
try:
    def cvrapi(cvr, country='dk', format='json'):
            request = urllib2.Request(
                    url='http://cvrapi.dk/api?search=%s&country=%s&format=%s' % (cvr, country, format),
                    headers={
                            'User-Agent': user_agent})
            with contextlib.closing(urllib2.urlopen(request)) as response:
                    return json.loads(response.read())
    print '\nData retrieved from CVR\n'
    
except Exception:
    pass
    print '\nFailed to get data from CVR\n'

#print result
result = cvrapi(cvrnr) #is dict is tested with print type(result)

del result['productionunits']
for key, value in result.iteritems() :
    print key, value

#then count the number of API requests
count = count +1

#for testing that the counters work
#print count
#print user_agent

#norwegian api test
#print(cvrapi(988615625, country=no))



# Copyright, Jack Andersen - Wisecloud.dk
# Coding: utf-8
import urllib2
import json
import contextlib
import collections
import csv

## define the main function
def cvrapi(cvr, country='dk', format='json'):
        request = urllib2.Request(
                url='http://cvrapi.dk/api?search=%s&country=%s&format=%s' % (cvr, country, format),
                headers={'User-Agent': str(user_agent) + user_suffix})
        with contextlib.closing(urllib2.urlopen(request)) as response:
                return json.loads(response.read())

##path variables
inPath = r'C:\Users\b020719\Downloads\CVR\virk.csv' #wgs84 EPSG:4326
#outPath = r'C:\Users\b020719\Desktop\test2.txt' #wgs84 EPSG:4326

##counters to allow more than 200 lookups per day.
#useragent needs to be a string i therefore count and set the suffix to abc.
user_agent = 1
user_suffix = 'abcd'
count = 0
rowcount = 0

#cvr to search for
cvrnr = None

#read file
try:
    with open(inPath, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rowcount = rowcount + 1
            cvrnr = None
            cvrnr = (int(row['cvr']))

            #print cvrnr
            print "\nLine " + str(rowcount) + " read from " + inPath + ":\n", "Found data for CVR " + str(cvrnr) +" ->"

            #print result
            result = cvrapi(cvrnr) #is dict is tested with print type(result) productionunits is list stored dict
            #print result
            del result['productionunits']
            for key, value in result.iteritems():
                        #print cvrnr.replace("[", "")
                        print key, value

                #for key in result['productionunits']:
                 #   print key

            #then count the number of API requests
            count = count +1

            #print cvrnr
            if count == 190:
               user_agent = user_agent + 1
               count = 0



except Exception:
    pass
    print "\nFailed to get data from " + inPath + "\n"

#for testing that the counters work
#print count
#print user_agent

#norwegian api test
#print(cvrapi(988615625, country=no))

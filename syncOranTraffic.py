'''
Created on 11 Mar 2018

@author: Lars Schotte
'''

from extraction import vnstattrafficdata, orangefupanalyzer
import httplib
import sys

srcipaddr = sys.argv[1]
srcdocument = sys.argv[2]

connection = httplib.HTTPConnection(srcipaddr)
connection.request("GET", srcdocument)
response = connection.getresponse()
vnstatdata = vnstattrafficdata.vnstattraffic(response.read())
connection.close()

orangefup = orangefupanalyzer.orangefup(vnstatdata.getDaily())

print orangefup.getCurrentFupUsageGiB()
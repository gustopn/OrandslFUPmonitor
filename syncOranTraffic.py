'''
Created on 11 Mar 2018

@author: Lars Schotte
'''

from extraction import vnstattrafficdata

# just for the sake of example we take our json files from a prepared /tmp file

currenttraficsourcefile = open("/tmp/orangedsl.txt", "r")
vnstatdata = vnstattrafficdata.vnstattraffic(currenttraficsourcefile.read())
currenttraficsourcefile.close()

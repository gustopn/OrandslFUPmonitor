'''
Created on 11 Mar 2018

@author: Lars Schotte
'''

import json

class vnstattraffic:
  
  def __init__(self, trafficdatajson):
    self.updated = None
    self.traffic = {}
    trafficdata = json.loads(trafficdatajson)
    if (len(trafficdata["interfaces"]) == 1):
      self.updated = trafficdata["interfaces"][0]["updated"]
      self.traffic["hourly"] = trafficdata["interfaces"][0]["traffic"]["hours"]
      self.traffic["daily"] = trafficdata["interfaces"][0]["traffic"]["days"]
      self.traffic["monthly"] = trafficdata["interfaces"][0]["traffic"]["months"]
  
  def getUpdated(self):
    return self.updated
  
  def getMonthly(self):
    return self.traffic["monthly"]
  
  def getDaily(self):
    return self.traffic["daily"]
  
  def getHourly(self):
    return self.traffic["hourly"]
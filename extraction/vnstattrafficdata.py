'''
Created on 11 Mar 2018

@author: Lars Schotte
'''

import json

class vnstattraffic:
  
  def __init__(self, trafficdatajson):
    self.__updated = None
    self.__traffic = {}
    trafficdata = json.loads(trafficdatajson)
    if (len(trafficdata["interfaces"]) == 1):
      self.__updated = trafficdata["interfaces"][0]["updated"]
      self.__traffic["hourly"] = trafficdata["interfaces"][0]["traffic"]["hours"]
      self.__traffic["daily"] = trafficdata["interfaces"][0]["traffic"]["days"]
      self.__traffic["monthly"] = trafficdata["interfaces"][0]["traffic"]["months"]
  
  def getUpdated(self):
    return self.__updated
  
  def getMonthly(self):
    return self.__traffic["monthly"]
  
  def getDaily(self):
    return self.__traffic["daily"]
  
  def getHourly(self):
    return self.__traffic["hourly"]
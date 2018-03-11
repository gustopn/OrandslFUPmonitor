'''
Created on 11 Mar 2018

@author: Lars Schotte
'''

class orangefup:
  
  def __init__(self, dailytraffic, billingdate=13, currentfupsetting=300.0):
    self.currentfupusage = 0
    self.orangefupsetting = currentfupsetting
    for daytraffic in dailytraffic:
      self.currentfupusage += int(daytraffic["rx"]) + int(daytraffic["tx"])
      if (daytraffic["date"]["day"] == billingdate):
        break
  
  def getCurrentFupUsage(self):
    return self.currentfupusage
  
  def getCurrentFupUsageGiB(self):
    return int( self.currentfupusage / 1024**2 )
  
  def getCurrentFupPercentage(self):
    return int( self.currentfupusage / self.orangefupsetting * 100 )
import time
from extrafunctions import checkTimeArraysEqual

"""Things to add:
-MultiThreading
-Finish method for getting the average post time for the most popular posts (custom time frame)
"""

class Analytic:
    def __init__(self, subreddit):
        self.subreddit = subreddit
    def gatherActiveUsers(self,hourIntervalToCheck,monthToStop,dayToStop, hourToStop):
        
        hourIntervalCount = 0
        intervalToCheck = hourIntervalToCheck*3600
        dateToEnd = [monthToStop,dayToStop,hourToStop]

        f = open((self.subreddit.display_name+".txt"),'a')
        f.write("Time Started"+str(time.localtime(time.time())[0:5])+"Interval checkingin secs: "+str(intervalToCheck)+"\n")
        print("Waiting")
        
        while not checkTimeArraysEqual(time.localtime(time.time())[1:4],dateToEnd):
            self.subreddit._fetch() #updates subreddits fields
            f.write("Hour ("+str(hourIntervalToCheck)+" hour) : "+str(hourIntervalCount)+" Active Users: "+str(self.subreddit.active_user_count)+"\n")
            time.sleep(intervalToCheck)
            hourIntervalCount += 1
        f.close()
    def avgTimePostedForPopularPosts(self):
        pass
    def readAnalytics(self, filePath):
        pass
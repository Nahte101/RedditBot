import time
import datetime
from extrafunctions import checkTimeArraysEqual

"""Things to add:
-MultiThreading
-Finish method for getting the average post time for the most popular posts (custom time frame)
-Reading analytics from file
"""

class Analytic:
    def __init__(self, subreddit):
        self.subreddit = subreddit
    def gatherActiveUsers(self,hourIntervalToCheck,monthToStop,dayToStop, hourToStop):
        
        hourIntervalCount = 0
        intervalToCheck = hourIntervalToCheck*3600
        dateToEnd = [monthToStop,dayToStop,hourToStop]

        f = open((self.subreddit.display_name+".txt"),'a')
        f.write("Time Started"+str(time.localtime(time.time())[0:5])+" Interval checking in secs: "+str(intervalToCheck)+"\n")
        print("Waiting")
        
        while not checkTimeArraysEqual(time.localtime(time.time())[1:4],dateToEnd):
            self.subreddit._fetch() #updates subreddits fields
            f.write("Hour ("+str(hourIntervalToCheck)+" hour) : "+str(hourIntervalCount)+" Active Users: "+str(self.subreddit.active_user_count)+"\n")
            time.sleep(intervalToCheck)
            hourIntervalCount += 1
        f.close()
    def avgTimePostedForPopularPosts(self,timeFrame, limit=100):
        topPosts = self.subreddit.top(time_filter=timeFrame,limit=limit)
        hourAvg = 0
        minuteAvg = 0
        postCount = 0
        for post in topPosts:
            postCount += 1
            utcDeltaTime = datetime.timedelta(seconds=post.created_utc)
            hourAvg += utcDeltaTime.seconds//3600
            minuteAvg += (utcDeltaTime.seconds//60)%60
        hourAvg /= postCount
        minuteAvg /= postCount
        print("Hour Avg: ",hourAvg," Minute Avg: ",minuteAvg)
    def readAnalytics(self, filePath=None):
        if (filePath == None):
            f = open((self.subreddit.display_name+".txt"),'r')
        else:
            f = open(filePath,'r')
        for line in str.splitlines(f.read()):
            print(line)
        f.close()
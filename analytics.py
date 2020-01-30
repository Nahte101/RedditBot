import time
from extrafunctions import checkTimeArraysEqual

class Analytic:
    def __init__(self, subreddit):
        self.subreddit = subreddit
    def gatherActiveUsers(self,monthToStop,dayToStop, hourToStop, minuteToStop):
        hours = 0
        dateToEnd = [monthToStop,dayToStop,hourToStop,minuteToStop]
        while not checkTimeArraysEqual(time.localtime(time.time())[1:5],dateToEnd):
            f = open((self.subreddit.display_name+".txt"),'a')
            f.write("Hour: "+str(hours)+" Active Users: "+str(self.subreddit.active_user_count)+",")
            time.sleep(3600)
            hours += 1
        f.close()
    def avgTimePostedForPopularPosts(self):
        pass
    def writeAnalytics(self):
        pass
    def readAnalytics(self, filePath):
        pass
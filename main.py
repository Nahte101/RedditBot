import praw
import time
from post import Poster
from analytics import Analytic
from threadManger import ThreadManager

reddit = praw.Reddit('personalAccount',
                        user_agent='Personal Account')
threads = ThreadManager()


def choice(subredditName=None,analysis=None,poster=None):
    
    if subredditName == None:
        subredditName = input("What subreddit to use? (Case sensitive) ")

    subreddit = reddit.subreddit(subredditName)
    
    if analysis == None:
        analysis = Analytic(subreddit)
    if poster == None:
        poster = Poster(subreddit)

    goodInput = False
    while not goodInput:
        option = input("Do you want to get statistics or post (1 or 2) ")
        if option == '1':
            
            while not goodInput:
                option = int(input('Track Active Users/Avg Time posted for popular posts/Read saved active user file (1/2/3) '))
                if option == 1:
                    month = int(input("What month would you like this to stop (num) "))
                    day = int(input("What day would you like this to stop "))
                    hour = int(input("What hour would you like this to stop (24 version) "))
                    hourInterval = int(input("How many times per hour should it check user count? "))
                    hourInterval = 1 / hourInterval

                    threadName = "Analysis Active Users"
                    threads.addThread(threadName,analysis.gatherActiveUsers,(hourInterval,month,day,hour))
                    threads.start(threadName)
                    goodInput = True
                elif option == 2:
                    timeFrame = input("What time frame would u like for popular posts? ")
                    postNum = int(input("How many posts will be used? "))
                    threadName = "Avg time for popular posts"
                    threads.addThread(threadName,analysis.avgTimePostedForPopularPosts, (timeFrame,postNum))
                    threads.start(threadName)
                    goodInput = True
                elif option == 3:
                    threadName = "Read Analytics"
                    threads.addThread(threadName,analysis.readAnalytics)
                    threads.start(threadName)
                    goodInput = True

        elif option == '2':

            title = input("What shall the title of the post be? ")

            goodInput = False

            timeDelayed = input("Would you like this to be time delayed? y/n ") == 'y'

            while not goodInput:

                postType = input("Image/Video/Text Post? (type img or vid or txt) ")

                if postType == 'img':
                    goodInput = True
                elif postType == 'vid':
                    goodInput = True
                elif postType == 'txt':
                    goodInput = True
                    

            if postType == 'txt':
                txt = input("What will the text be below title? ")
                if timeDelayed:
                    timeToPost = input("Time to be posted (AU Time) mm:dd:hh:mm ")
                    dateToPost = timeToPost.split(":")

                    threadName = "Delay Txt post"
                    threads.addThread(threadName,poster.delayPost,(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,txt))
                    threads.start(threadName)
                else:
                    threadName = "Txt Post"
                    threads.addThread(threadName,poster.postTxt,(txt,title))
                    threads.start(threadName)
            else:
                directory = input("Directory to file: ")
                thumbnail = None

                if input("Would u like a thumbnail? y/n ") == 'y':

                    thumbnail = input("Directory to thumbnail: ")

                if timeDelayed:

                    time_to_post = input("Time to be posted (AU Time) mm:dd:hh:mm ")
                    dateToPost = time_to_post.split(":")

                    if postType == 'img':
                        threadName = "Delay img Post"
                        threads.addThread(threadName,poster.delayPost,(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,None,directory))
                        threads.start(threadName)
                    else:
                        threadName = "Delayed vid post"
                        threads.addThread(threadName,poster.delayPost,(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,None,directory,thumbnail))
                        threads.start(threadName)
                else:
                    if postType == 'img':
                        threadName = "Img post"
                        threads.addThread(threadName,poster.postImg,(directory,title))
                        threads.start(threadName)
                    else:
                        threadName = "Vid post"
                        threads.addThread(threadName,poster.postVid,(directory,title,thumbnail))
                        threads.start(threadName)
                 
        #still neeed to add threading to methods called
        anotherGo = input("Would you like to do another operation? y/n ") == 'y'
        if anotherGo:
            choice()
        else:
            print("Waiting for threads to finish")
            threads.focusAllThreads()
            print("All threads finished")

if __name__ == "__main__":
    choice()
    

    


import praw
import time
from post import Poster
from analytics import Analytic

if __name__ == "__main__":
    
    reddit = praw.Reddit('personalAccount',
                        user_agent='Personal Account')

    subredditName = input("What subreddit to use? (Case sensitive) ")

    subreddit = reddit.subreddit(subredditName)

    goodInput = False
    while not goodInput:
        choice = input("Do you want to get statistics or post (1 or 2) ")
        if choice == '1':
            month = int(input("What month would you like this to stop (num) "))
            day = int(input("What day would you like this to stop "))
            hour = int(input("What hour would you like this to stop (24 version) "))
            hourInterval = int(input("How many times per hour should it check user count? "))
            hourInterval = 1 / hourInterval
            analysis = Analytic(subreddit)
            analysis.gatherActiveUsers(hourInterval,month,day,hour)
            goodInput = True

        elif choice == '2':

            poster = Poster(subreddit)

            title = input("What shall the title of the post be? ")

            goodInput = False

            timeDelayed = input("Would you like this to be time delayed? True or False (Case Sensitive) ") == 'True'

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
                    poster.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,txt=txt)
                else:
                    poster.postTxt(txt,title)
            else:
                directory = input("Directory to file: ")
                if timeDelayed:
                    time_to_post = input("Time to be posted (AU Time) mm:dd:hh:mm ")
                    dateToPost = time_to_post.split(":")
                    if postType == 'img':
                        poster.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,filePath=directory)
                    else:
                        poster.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,filePath=directory)
                else:
                    if postType == 'img':
                        poster.postImg(directory,title)
                    else:
                        poster.postVid(directory,title)


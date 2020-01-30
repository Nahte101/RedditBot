import praw
import time
from post import Post
from analytics import Analytic
if __name__ == "__main__":
    
    reddit = praw.Reddit(client_id='msA8YHPtMopEFg'
                        ,client_secret='iiqKiuOkS4bicJwyBiTq_hQ5lwQ',
                        username='Nahte101',
                        password='pokemon101',
                        user_agent='idk')

    subredditName = input("What subreddit to use? (Case sensitive) ")

    subreddit = reddit.subreddit(subredditName)

    goodInput = False
    while not goodInput:
        choice = input("Do you want to get statistics or post (1 or 2) ")
        if choice == '1':
            month = int(input("What month would you like this to stop (num) "))
            day = int(input("What day would you like this to stop "))
            hour = int(input("What hour would you like this to stop (24 version) "))
            minute = int(input("What minute would you like this to stop "))
            analysis = Analytic(subreddit)
            analysis.gatherActiveUsers(month,day,hour,minute)

        elif choice == '2':

            post = Post(subreddit)

            title = input("What shall the title of the post be? ")

            goodInput = False

            timeDelayed = bool(input("Would you like this to be time delayed? True or False (Case Sensitive) "))

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
                    post.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,txt=txt)
                else:
                    post.postTxt(txt,title)
            else:
                directory = input("Directory to file: ")
                if timeDelayed:
                    time_to_post = input("Time to be posted (AU Time) mm:dd:hh:mm ")
                    dateToPost = time_to_post.split(":")
                    if postType == 'img':
                        post.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,filePath=directory)
                    else:
                        post.delayPost(dateToPost[0],dateToPost[1],dateToPost[2],dateToPost[3],postType,title,filePath=directory)
                else:
                    if postType == 'img':
                        post.postImg(directory,title)
                    else:
                        post.postVid(directory,title)


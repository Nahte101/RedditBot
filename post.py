import praw
import time
from extrafunctions import checkTimeArraysEqual
from threadManger import ThreadManager

"""Things to add
-MultiThreading
-MultiProcessing"""

class Post:#An object that stores a post
    def __init__(self,title,postType=None,txt=None,filePath=None):
        self.title = title
        self.postType = postType
        self.txt = txt
        self.filePath = filePath
    
class Poster:#Object that posts
    def __init__(self, subreddit):
        self.subreddit = subreddit

    def postImg(self, imgPath,title):
        self.subreddit.submit_image(title=title, image_path=imgPath,without_websockets=True)

    def postVid(self, vidPath, title,thumbnail=None):
        self.subreddit.submit_video(title=title, video_path=vidPath,without_websockets=True,thumbnail_path=thumbnail)

    def postTxt(self,txt,title):
        self.subreddit.submit(title=title,selftext=txt)
    
    def post(self,postObj):#For posting Post objects
        if postObj.postType == "img":
            self.postImg(postObj.filePath,postObj.title)
        elif postObj.postType == 'vid':
            self.postVid(postObj.filePath,postObj.title)
        else:
            self.postTxt(postObj.txt,postObj.title)

    def postMultipleEveryTimeInterval(self,listOfPosts,HourlyIntervalToPost):#Post each post every HourlyIntervalToPost
        for post in listOfPosts:
            time.sleep(HourlyIntervalToPost*3600)
            self.post(post)

    def postMultiple(self,listOfPosts):
        for post in listOfPosts:
            self.post(post)
    def delayPost(self,monthToPost,dayToPost,hourToPost,minuteToPost,postType,title,txt=None,filePath=None,thumbnailPath=None):
        
        notPosted = True
        dateToPost = [monthToPost,dayToPost,hourToPost,minuteToPost]
        
        while notPosted:

            currentTime = time.localtime(time.time())
            currentDateTime = currentTime[1:5]
            time.sleep(0.5)
            
            if checkTimeArraysEqual(dateToPost,currentDateTime):
                if postType == 'txt':
                    self.postTxt(txt,title)
                    notPosted = False
                    print('posted')
                elif postType == 'img':
                    self.postImg(filePath,title)
                    notPosted = False
                    print('posted')
                elif postType == 'vid':
                    self.postVid(filePath,title,thumbnailPath)
                    notPosted = False
                    print('posted')
                else:
                    print("Invalid Post Type : ",str(postType))


    
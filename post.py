import praw
import time
from extrafunctions import checkTimeArraysEqual

class Post:
    def __init__(self, subreddit):
        self.subreddit = subreddit
    
    def postImg(self, imgPath,title):
        self.subreddit.submit_image(title=title, image_path=imgPath,without_websockets=True)
    
    def postVid(self, vidPath, title):
        self.subreddit.submit_video(title=title, video_path=vidPath,without_websockets=True)
    
    def postTxt(self,txt,title):
        self.subreddit.submit(title=title,selftext=txt)

    def delayPost(self,monthToPost,dayToPost,hourToPost,minuteToPost,postType,title,txt=None,filePath=None):
        
        notPosted = True
        dateToPost = [monthToPost,dayToPost,hourToPost,minuteToPost]
        print("Waiting")
        while notPosted:

            currentTime = time.localtime(time.time())
            currentDateTime = currentTime[1:5]
            time.sleep(0.5)
            
            if checkTimeArraysEqual(dateToPost,currentDateTime):
                if postType == 'txt':
                    self.postTxt(txt,title)
                    notPosted = False
                    print('posted')
                if postType == 'img':
                    self.postImg(filePath,title)
                    notPosted = False
                    print('posted')
                elif postType == 'vid':
                    self.postVid(filePath,title)
                    notPosted = False
                    print('posted')
                else:
                    print("Invalid Post Type")


    
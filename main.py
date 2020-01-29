import praw
import time


reddit = praw.Reddit(client_id='msA8YHPtMopEFg'
                    ,client_secret='iiqKiuOkS4bicJwyBiTq_hQ5lwQ',
                    username='Nahte101',
                    password='pokemon101',
                    user_agent='idk')

subreddit_name = input("What subreddit to post to? (Case sensitive) ")

subreddit = reddit.subreddit(subreddit_name)


title = input("What shall the title of the post be? ")

good_input = False

while not good_input:
    post_type = input("Image/Video/Text Post? (type img or vid or txt) ")
    if post_type == 'img':
        good_input = True
    elif post_type == 'vid':
        good_input = True
    elif post_type == 'txt':
        good_input = True


if post_type == 'txt':
    nonTitleText = input("What will the text be below title? ")
else:
    directory = input("Directory to file: ")

time_to_post = input("Time to be posted (AU Time) mm:dd:hh:mm ")



date_to_post = time_to_post.split(":")

def checkTimeArraysEqual(arr1,arr2):#must be of same length
    match = True
    for i in range(0,len(arr2)):
        if int(arr1[i]) != int(arr2[i]):
            match = False
            break
    return match

print("Waiting")

not_posted = True

while not_posted:
    currenttime = time.localtime(time.time())
    currentdatetime = currenttime[1:5]
    if checkTimeArraysEqual(date_to_post,currentdatetime):
        if post_type == 'img':
            post = subreddit.submit_image(title=title, image_path=directory,without_websockets=True)
            f = open((subreddit_name+".txt"),'w')
            f.write(post.flair.choices())
            f.close()
            not_posted = False
            print('posted')
        elif post_type == 'vid':
            post = subreddit.submit_video(title=title, video_path=directory,without_websockets=True)
            f = open((subreddit_name+".txt"),'w')
            f.write(post.flair.choices())
            f.close()
            not_posted = False
            print('posted')
        elif post_type == 'txt':
            post = subreddit.submit(title=title,selftext=nonTitleText)
            not_posted = False
            f = open((subreddit_name+".txt"),'w')
            f.write(post.flair.choices())
            f.close()
            print('posted')

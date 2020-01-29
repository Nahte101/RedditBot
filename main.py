import praw
import time

def checkTimeArraysEqual(arr1,arr2):#must be of same length
    match = True
    for i in range(0,len(arr2)):
        if int(arr1[i]) != int(arr2[i]):
            match = False
            break
    return match

def post(subreddit):

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

    not_posted = True
    print("Waiting")

    while not_posted:
        currenttime = time.localtime(time.time())
        currentdatetime = currenttime[1:5]
        if checkTimeArraysEqual(date_to_post,currentdatetime):
            if post_type == 'img':
                subreddit.submit_image(title=title, image_path=directory,without_websockets=True)
                not_posted = False
                print('posted')
            elif post_type == 'vid':
                subreddit.submit_video(title=title, video_path=directory,without_websockets=True)
                not_posted = False
                print('posted')
            elif post_type == 'txt':
                subreddit.submit(title=title,selftext=nonTitleText)
                not_posted = False
                print('posted')

def write_file_stats(subreddit,month_to_stop,day_to_stop, hour_to_stop, minute_to_stop):
    hours = 0
    while not (int(time.localtime(time.time())[1]) == month_to_stop and int(time.localtime(time.time())[2]) == day_to_stop and int(time.localtime(time.time())[3]) == hour_to_stop):
        f = open((subreddit_name+".txt"),'a')
        f.write("Hour: "+str(hours)+" Active Users: "+str(subreddit.active_user_count)+",")
        time.sleep(3600)
        hours += 1
    f.close()

reddit = praw.Reddit(client_id='msA8YHPtMopEFg'
                    ,client_secret='iiqKiuOkS4bicJwyBiTq_hQ5lwQ',
                    username='Nahte101',
                    password='pokemon101',
                    user_agent='idk')

subreddit_name = input("What subreddit to use? (Case sensitive) ")

subreddit = reddit.subreddit(subreddit_name)
good_input = False
while not good_input:
    choice = input("Do you want to get statistics or post (1 or 2) ")
    if choice == '1':
        good_input = True
        month = int(input("What month would you like this to stop (num) "))
        day = int(input("What day would you like this to stop "))
        hour = int(input("What hour would you like this to stop (24 version) "))
        minute = int(input("What minute would you like this to stop "))
        write_file_stats(subreddit,month,day, hour, minute)
    elif choice == '2':
        good_input = True
        post(subreddit)


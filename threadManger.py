import threading
from threading import Thread

class ThreadManager:
    def __init__(self):
        self.threads = {}
    def flagAsQuittable(self,threadName):#sets thread to daemon so program can be quitted
        self.threads[threadName].daemon = True
    def flagAllAsQuittable(self):#sets all threads to daemon so when main program exits program completes
        for thread in self.threads:
            thread.daemon = True
    def focusThread(self,threadName):#Focuses a thread to finish it before doing anything after it
        self.threads[threadName].join()
    def focusAllThreads(self):
        for key in self.threads.keys():
            self.threads[key].join()
            print(str(key))
    def start(self, threadName):
        self.threads[threadName].start()
    def startAll(self):
        for thread in self.threads:
            thread.start()
    def addThread(self,threadName, targetFunc, args=()):
        print("Adding  thread: ",threadName)
        self.threads[threadName] = Thread(name=threadName,target=targetFunc,args=args)
    def addThreadObj(self,thread):
        self.threads[thread.name] = thread
    def isThreadAlive(self, threadName):
        return self.threads[threadName].is_alive()
    def removeThread(self,threadName):
        self.threads.pop(threadName)

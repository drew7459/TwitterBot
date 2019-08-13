import tweepy
import time
from chatBot import genResponse
from keys import *
from replyMentions import reply_to_tweets
from post import createTweet
import random
import sys
import argparse

def start(amount, randNum, days):
    print("inside start")
    if(randNum == 1):
        print("random post")
        for x in range(days):
            randPost(amount)
    else:
        print("even post")
        for x in range(days):
            even(amount)
        
def even(amount):
    print(86400/amount)
    time.sleep(86400/amount)
    actions()
        
#Post and reply to tweets at random times during day
#amount specifies how many times during the day
def randPost(amount):
    arr = []
    count = 1
    
    for x in range(amount):
        arr.append(random.randint(0,86400))

    arr.sort()
    print(arr)
    start_time = time.time()
    time.sleep(arr[0])
    actions()
    
    while(count < amount):
        time.sleep(arr[count] - arr[count - 1])
        actions()

    elapsed_time = time.time() - start_time
    
    if(elapsed_time < 86400):
        time.sleep(86400 - elapsed_time)

def actions():
    createTweet()
    reply_to_tweets()
        
def checkInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

print(str(sys.argv))
    
for arg in sys.argv[1:]:
    if not checkInt(arg):
        sys.exit("All arguments must be integers. Exit")
    
if(int(sys.argv[2]) == 0 or int(sys.argv[2]) == 1): 
    start(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
else:
    sys.exit("Arg2 must be either 1 or 0 (true or false)")

        

import tweepy
import time
from chatBot import genResponse
from keys import *
from replyMentions import reply_to_tweets
from post import createTweet
import random

def start(amount, randNum, days):
    if(randNum):
        for x in range(days):
            randPost(amount)
    else:
        for x in range(days):
            even(amount)
        
def even(amount):
    sleep(86400/amount)
    actions()
        
#Post and reply to tweets at random times during day
#amount specifies how many times during the day
def randPost(amount):
    arr = []
    count = 1
    
    for x in range(amount):
        arr.append(random.randint(0,86400))
        
    arr.sort()
    
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
        
        
        

        

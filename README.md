# Twitter Bot

Twitter Bot is a bot that can post and reply to mentions on twitter.
It uses [ChatterBot](https://github.com/gunthercox/ChatterBot) for replying and [tweepy](https://github.com/tweepy/tweepy) for connecting to twitter.

## Getting Started
### Installation

* Install chatterbot and dependencies [https://github.com/gunthercox/ChatterBot](https://github.com/gunthercox/ChatterBot)
* Install tweepy and dependencies [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy)

        pip install chatterbot
        pip install tweepy

* Clone this repo:

        git clone https://github.com/drew7459/TwitterBot.git
        cd TwitterBot/TwitterBot
	
### Developer Account
Make a developer twitter account if you do have one already then skip this step 

* Go to the [twitter dev website](https://developer.twitter.com/en/apps)
* Sign into the account that you want to make your bot on
* Open apps on the top right corner under the drop down of your name
* Create an app
* Fill out the information and then submit
* Open Keys and Tokens

### Configure TwitterBot
####Twitter Python Scripts
* Open Keys and Tokens from the developer account
* Go to keys.py and input Keys and Tokens

####ChatterBot Python Scripts


### Run.py
Run.py uses command line arguments so when running input the following parameters in the exact order

* Input parameters
	* Amount of Tweets per day
	* Binary true or false for random times
	* Amount of days to run

Sample Input for 3 tweets, at random times, for 2 days.
         
        python run.py 3 1 2

# Twitter Bot

Twitter Bot is a bot that can post and reply to mentions on twitter.
It uses [ChatterBot](https://github.com/gunthercox/ChatterBot) for replying and [tweepy](https://github.com/tweepy/tweepy) for connecting to twitter.

## Getting Started
### Installation

* Install chatterbot and dependencies [https://github.com/gunthercox/ChatterBot](https://github.com/gunthercox/ChatterBot)
* Install tweepy and dependencies [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy)

```bash
pip install chatterbot
pip install tweepy
```
* Clone this repo:
```bash
git clone https://github.com/drew7459/TwitterBot.git
cd TwitterBot/TwitterBot
```
### Run.py
* Input parameters through command line args
	* Amount of Tweets per day
	* Binary true or false for random times
	* Amount of days to run

Sample Input for 3 tweets, at random times, for 2 days
```bash
python run.py 3 1 2
```
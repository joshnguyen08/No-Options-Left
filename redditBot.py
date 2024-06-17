import praw
import os

client_id = os.environ.get("clientID")
client_secret = os.environ.get("RedditSecretID")
password = os.environ.get("redditPWD")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="windows:com.example.myredditapp:v1.2.3 (by /u/NoOptionsLeft0)",
    username="NoOptionsLeft0",
)

def post_to_subreddit(subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        print(f"Posted to {subreddit_name}: {title}")
    except Exception as e:
        print(f"An error occured: {e}")

subreddits = ['PrizePicksPlays' , 'PRIZEPICKSBESTPICK', 'OptionsOnly', 
              'RealDayTrading' , 'EducatedInvesting' , 'StonkTraders', 'EliteTraders',
               'UltimateTraders', 'hot_stocks', 'Stocks_Picks' , 
                   'IndianStocks', 'BreakoutStocks' , 'squeeze_stocks' ,
                   'PrizePicksDemonTime'
                   ]
title = "FREE PLACE TO WIN AND EAT!💸💸💸💸💸"
body = """
Hello everyone, 

I wanted to offer a FREE and amazing server to discuss the topics of prizepicks play and options trading


Join here on dis(cord): TdEyQqwxp2

**Everything is free** JOIN THE COMMUNITY TODAY!!"""

for subreddit in subreddits:
    post_to_subreddit(subreddit, title, body)
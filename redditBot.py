import praw
import os
import time
import random

client_id = os.environ.get("clientID")
client_secret = os.environ.get("RedditSecretID")
password = os.environ.get("redditPWD")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="windows:com.example.myredditapp:v1.2.3 (by /u/No-OptionsLeft)",
    username="No-OptionsLeft",
)

def vary_content(base_text, variations):
    return base_text + " " + random.choice(variations)

title_variations = [
    "Join us now for the best tips!",
    "Don't miss out on winning strategies!",
    "Expert advice and community support!",
    "Learn and earn with us!",
    "Get your best picks here!"
]

body_variations = [
    "\nWe share the best strategies for success. ",
    "\nCome and be part of a winning community.",
    "\nJoin now and start earning today!",
    "\nExpert insights and community discussions. ",
    "\nDon't miss your chance to improve your game! "
]


def post_to_subreddit(subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        print(f"Posted to {subreddit_name}: {title}")
    except Exception as e:
        print(f"An error occured: {e}")

subreddits = ['PRIZEPICKSBESTPICK', 'OptionsOnly', 
               'StonkTraders', 'EliteTraders',
               'UltimateTraders', 'Stocks_Picks' , 
                 'BreakoutStocks' , 'squeeze_stocks' ,
                   'PrizePicksDemonTime' , 'PrizePicksPlays' , 'BettingPicks' , 'SportsBettingPicks',
                   'TheBettingGuru' , 'SportsBettingExperts', 'FanduelBettingLocks', 
                   ]
base_title = "FREE PLACE TO WIN AND EAT!💸💸💸💸💸"
base_body = """
Hello everyone, 

I wanted to offer a FREE and amazing server to discuss the topics of prizepicks play and options trading


Join here on dis(cord): TdEyQqwxp2

**Everything is free** JOIN THE COMMUNITY TODAY!!"""

for subreddit in subreddits:
    varied_title = vary_content(base_title, title_variations)
    varied_body = vary_content(base_body, body_variations)
    post_to_subreddit(subreddit, varied_title, varied_body)

    time.sleep(random.randint(30,60))

print("All Posted")

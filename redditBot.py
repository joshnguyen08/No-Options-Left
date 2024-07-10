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
    user_agent="windows:com.example.myredditapp:v1.2.3 (by /u/NoOptionsLeft0)",
    username="NoOptionsLeft0",
)


"""def vary_content(base_text, variations):
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
]"""


def post_to_subreddit(subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        print(f"Posted to {subreddit_name}: {title}")
    except Exception as e:
        print(f"An error occured: {e} with {subreddit_name}")

subreddits = [
             'SportsBettingPicks',
            'TheBettingGuru' , 'FanduelBettingLocks'
            ,'OnlineCasinoGambling' , 'GamblingBros', 'sportsgambling', 'OptionsOnly', 
            'StonkTraders', 'SolanaMemeCoins', 'memecoinmoonshots',
             'Memecoinhub' , 'investment' ,'gme_meltdown',
            'StockMarketChat', 'forex_trades', 'ForexForALL', 
            '10xPennyStocks', 'TopPennyStocks', 'PennyStocksCanada', 'Pennystock', 'PennyStocksWatch',
            'MMAbetting', 'matchedbetting', 'cryptotrading', 'CryptoTradingFloor',
            'portfolios', 'AusFinance', 'ConcentrationOfWealth', 'WealthMindset', 'SolanaMemeCoins','AnyAdvertise','StonkTraders','StonkFeed','CryptoMarkets',
             'Buttcoin', 'btc','CryptoTechnology',
           'SHIBArmy','CryptoApeing','SweepSlotsCasino', 'PRIZEPICKSBESTPICK','OnlineSlotCasinos','UltimateTraders','BreakoutStocks' , 'squeeze_stocks',
           ]
#'PrizePicksDemonTime' , 'PrizePicksPlays' ,
base_title = ["FREE PLACE TO WIN AND EAT!💸💸💸" , "🤑🤑Join Our Community for Expert Tips on Betting, Trading, and Crypto💸💰💰💸",
              "🤑🤑Unlock the Secrets to Successful Trading and Betting with Us!💰💰💰", "🏦Your Hub for PrizePicks, Trading Strategies, and Crypto Insights🏦",
              "🏦Sports Betting, Trading, and Crypto: Join Our Free Discussion!🏦", "🏦Maximize Your Gains: From Options Trading to Meme Coins to Sports Betting🏦",
               "Discover Winning Strategies in Betting, Trading, and Crypto🏧🏧🏧", "Community Insights on PrizePicks, Options, and Crypto Trends📈📈📈", 
                "From Sports Bets to Crypto Gains: Join the Discussion📊📊📊","All-in-One Community for Trading, Betting, and Crypto Enthusiasts🧑‍🔬🧑‍🔬🧑‍🔬"  ]
base_body = [ 

"""Hello everyone🤑,

Join our FREE and amazing server to discuss betting, gambling, and becoming rich! 

We offer top stock picks, the best options trading plays, PrizePicks locks, and a chance to hit big on meme coins. 

Join us on Discord: TdEyQqwxp2

 Everything is free - Join the community today!""",

"""Discover the best tips for betting, trading, and growing your wealth in our FREE server! 🏦

We provide top stock picks, options trading plays, PrizePicks locks, and meme coin advice. 

Join our community on Discord: TdEyQqwxp2

 Everything is free - Join now!""",

"""Unlock your potential and join our FREE server to master betting, trading, and wealth-building strategies!🏦

 Gain exclusive access to top stock picks, winning options plays, PrizePicks locks, and opportunities to hit big on meme coins. 
 
 Don't miss out - join us on Discord: TdEyQqwxp2
 
 Everything is free - Take the first step to financial success today!""",

 """Hey there,

Transform your financial future by joining our FREE server! 🏦


Discover the best betting tips, profitable trading strategies, and insights on PrizePicks and meme coins. 

Elevate your game and connect with like-minded individuals. 

Don't wait to join us now on Discord: TdEyQqwxp2 \nStart your journey to wealth today!""",

"""Seize the opportunity to grow your wealth with our FREE server! 🏦


Get exclusive top stock picks, powerful options trading strategies, unbeatable PrizePicks locks, and the latest on meme coins. 

Don't wait - join our vibrant community on Discord: TdEyQqwxp2

 Your path to financial freedom starts here!""",

 """Elevate your betting and trading skills by joining our FREE and dynamic server! 🏦
 
 Access top-notch stock picks, expert options trading plays, reliable PrizePicks locks, and lucrative meme coin tips. 
 
 Join the movement and connect with winners on Discord: TdEyQqwxp2
 
 Make the leap to financial success today!
""",
"""
Hello everyone, 🏦🏦

I wanted to offer a FREE and amazing server to discuss the topics betting, gambling, and becoming rich🤑🤑!


WE OFFER:

Top stocks pick for long-term growth📈📈

Best options trading plays💰💰💰

Prizepicks locks 🔒🔒🔒

Chance to hit big on meme coins! 🪙🪙🪙

⬇️⬇️⬇️⬇️JOIN NOW ⬇️⬇️⬇️⬇️

Join here on dis(cord): TdEyQqwxp2

**Everything is free** JOIN THE COMMUNITY TODAY!!"""
 ]

for subreddit in subreddits:

    varied_title = random.choice(base_title)
    varied_body = random.choice(base_body)
    post_to_subreddit(subreddit, varied_title, varied_body)

    time.sleep(random.randint(45,70))

print("All Posted")

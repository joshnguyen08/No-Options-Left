import os
import tweepy
import random
import time
import sys

# Retrieve the API keys and tokens from environment variables
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Check if any of the API keys or tokens are None
if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN]):
    print("One or more environment variables are missing.")
    sys.exit(1)

# Authenticate to Twitter using Client for v2
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Authenticate to Twitter using API for v1.1 (for media upload)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Directory containing images
GALLERY_DIR = os.getenv('TWITTER_GALLERY_DIR')

# Base texts for tweets
base_texts = [
    "GUARENTEED LOCKS... WE DON'T MISS.\n\nFREE, JOIN TODAY..\n\n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷📷 #soccer #easymoney #parley #betting #win #sportspick #DFS #fantasy #cashprizes\n\nJOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    "CASH IT!!! 🔥🔥🔥\n\nANOTHER FIRE CALLOUT FOR THE DISCORD\n\nhttps://discord.gg/tWTZufybQ8\n\n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷 #soccer #easymoney #parley #betting #win #wingbig #sportspick #fantasysports #DFS #fantasy #cashprizes",
    "BANG!!! CASH THIS... FREE CALLOUTS IN THE DISCORD. \n\nJOIN TODAY!\n\nPREMIUM IS FREE, ALL YOU HAVE TO DO IS FOLLOW!\nJOIN HERE ⬇️\nhttps://discord.gg/fDmVwEZYu4\n\n#sportsbettor , #optionstrading , #gme , #amc , #prizepicks #nba #cash #money",
    "Nothing but consistency green slips in the discord\n\n JOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    "OPTIONS, SPORTS BETTING, INVESMENTS, WE GOT IT ALL..\n \n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷📷 #soccer #easymoney #parley #betting #win #sportspick #DFS #fantasy #cashprizes\nJOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    "WE CAN'T MISS AT ALL IN ANY REALMS\n \n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷📷 #soccer #easymoney #parley #betting #win #sportspick #DFS #fantasy #cashprizes\nJOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    "JOIN OUR WHOLESOME COMMUNITY TODAY! \n\n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷📷 #soccer #easymoney #parley #betting #win #sportspick #DFS #fantasy #cashprizes\nJOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    "PROFESSIONAL AND FREE COMMUNITY FOR WINNERS \n\n#PrizePickscfb #sportsbetting #stocks #options #prizepicks #nba📷📷 #soccer #easymoney #parley #betting #win #sportspick #DFS #fantasy #cashprizes\nJOIN HERE ⬇️\nhttps://discord.gg/TdEyQqwxp2",
    """WE OFFER:

Top stocks pick for long-term growth📈📈

Best options trading plays💰💰💰

Prizepicks locks 🔒🔒🔒

Chance to hit big on meme coins! 🪙🪙🪙

⬇️⬇️⬇️⬇️JOIN NOW ⬇️⬇️⬇️⬇️

Join here on dis(cord): TdEyQqwxp2""",


]

def tweet_image(image_path):
    caption = random.choice(base_texts)  # Choose a random base text
    
    # Upload media
    media = api.media_upload(image_path)
    
    # Create tweet with media
    response = client.create_tweet(text=caption, media_ids=[media.media_id_string])
    print(f'Tweeted: {response.data}')

def main():
    images = os.listdir(GALLERY_DIR)
    files = []
    for file in images:
        full_path = os.path.join(GALLERY_DIR, file)
        if os.path.isfile(full_path):
            files.append(file)
    
    
    if not files:
        print("No files found in the directory.")
        return

    while True:
        random_file = random.choice(files)
        random_file_path = os.path.join(GALLERY_DIR, random_file)
        
        if os.path.isfile(random_file_path):
            tweet_image(random_file_path)
            print(f'Tweeted: {random_file_path}')
            delay = random.randint(180, 360)
            print(f'Waiting for {delay} seconds before the next tweet...')
            time.sleep(delay)
        else:
            print(f'Image not found: {random_file_path}')
            
if __name__ == "__main__":
    main()

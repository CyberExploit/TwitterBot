import tweepy
import time

# Import our Twitter credentials from credentials.py
from conf import consumer_key, consumer_secret, access_token, access_token_secret

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #cybersecurity, limit to 10
try:

	for tweet in tweepy.Cursor(api.search,q='#cybersecurity',lang = "en", include_rts=False).items(10):
		try:
			followers = tweet.user.followers_count
			if followers < 1000 :
				if "RT" not in tweet.text and not tweet.retweeted:
					print('Tweet by: @%s' % tweet.user.screen_name)
					print('Followed by: ~%s' % tweet.user.followers_count)
		        		# Favorite the tweet
				        tweet.favorite()
					# Retweet
					tweet.retweet()
	        			print('Favorited and retweet the tweet')
		        		# Follow the user who tweeted
	        			tweet.user.follow()
			        	print('Followed the user')
					time.sleep(180)

		except Exception as e:
			print e.message
			time.sleep(60)
except tweepy.error.TweepError as e:
	print e.keys()

except Exception as e:
	print e

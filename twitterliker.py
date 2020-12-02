import tweepy
import time

auth = tweepy.OAuthHandler('enter your keys from developer twitter','right here')
auth.set_access_token('access tokens','go here')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '100daysofcode'
numTweets = 250

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
	try: 
		print('Liked')
		tweet.favorite()
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

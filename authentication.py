import tweepy
def auth():
	# once you have registered for API, you can
	# find 'em keys at https://apps.twitter.com while you are logged in with your account
	# then click the API
	# go-to "Keys and Access Tokens" tab for your keys and stuff
	consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxx" # API Key
	consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # API Secret
	# copy-paste the whole key wheather its like:- xxxxxxxxx-xxxxxxxxxxxxxxx
	access_token = "xxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

	try:
		# initialize the Oauth object for OAuthHandler class in tweepy module
		# parameters are consumer key, consumer_secret and callback(optional)
		Oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		Oauth.set_access_token(access_token, access_token_secret)
		username = tweepy.OAuthHandler.get_username(Oauth)
		api = tweepy.API(Oauth)
		return username
	except tweepy.TweepError:
		return 0
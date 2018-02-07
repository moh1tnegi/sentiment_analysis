def auth():
	# once you have registered for an API, you can
	# find 'em keys at https://apps.twitter.com while you are logged in with your account
	# then click the API
	# go-to "Keys and Access Tokens" tab for your keys and stuff
	consumer_key = "your_consumer_key" # API Key
	consumer_secret = "your_consumer_secret" # API Secret

	access_token = "your_access_token"
	access_token_secret = "your_access_token_secret"

	try:
		# initialize the Oauth object for OAuthHandler class in tweepy module
		# parameters are consumer key, consumer_secret and callback(optional)
		Oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		tweepy.Oauth.set_access_token(access_token, access_token_secret)
		username = tweepy.OAuth.get_username()
		API = tweepy.API(Oauth)
		return username

	except:
		print("Authentication Error!")

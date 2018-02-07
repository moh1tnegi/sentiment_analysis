def auth():
	# once you have registered for an API, you can
	# find 'em keys at https://apps.twitter.com while you are logged in with your account
	# then click the API
	# go-to "Keys and Access Tokens" tab for your keys and stuff
	consumer_key = "UqPjzsEsx5MZIUYgX2YeKYg94" # API Key
	consumer_secret = "Fzo8L6h1Z3HGWCrDRpMFAVAE63ZhLLtfJQnV2r5sOaO2HQnx18" # API Secret

	access_token = "gWBtA8OJ6klrHtVlEoiBtlekE6BFlDb"
	access_token_secret = "raDruNwLV7rcj2pobmXWMJ9fVQevWJIfpCq5q1MqrSkLM"

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

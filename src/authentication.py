from tweepy import OAuthHandler, API, TweepError


def auth():
    """ once you have registered for API, you can
        find 'em keys at https://apps.twitter.com while you are logged in with your account
        then click the API
        go-to "Keys and Access Tokens" tab for your keys and stuff."""
    consumer_key = "UqPjzsEsx5MZIUYgX2YeKYg94"  # API Key
    consumer_secret = "Fzo8L6h1Z3HGWCrDRpMFAVAE63ZhLLtfJQnV2r5sOaO2HQnx18"  # API Secret
    # copy-paste the whole key wheather its like:- xxxxxxxxx-xxxxxxxxxxxxxxx
    access_token = "763711848747241472-gWBtA8OJ6klrHtVlEoiBtlekE6BFlDb"
    access_token_secret = "raDruNwLV7rcj2pobmXWMJ9fVQevWJIfpCq5q1MqrSkLM"

    try:
        # initialize the Oauth object for OAuthHandler class in tweepy module
        # parameters are consumer key, consumer_secret and callback(optional)
        oauth = OAuthHandler(consumer_key, consumer_secret)
        oauth.set_access_token(access_token, access_token_secret)
        username = OAuthHandler.get_username(oauth)
        api = API(oauth)
        yield api
        yield username
    except TweepError:
        return 0

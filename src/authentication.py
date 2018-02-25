from tweepy import OAuthHandler, API, TweepError


def auth():
    """ once you have registered for API, you can
        find 'em keys at https://apps.twitter.com while you are logged in with your account
        then click the API
        go-to "Keys and Access Tokens" tab for your keys and stuff."""
    consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"  # API Key
    consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # API Secret
<<<<<<< HEAD
    # copy-paste the whole key wheather its like:- xxxxxxxxx-xxxxxxxxxxxxxxx or whatever
=======
    # copy-paste the whole key wheather its like:- xxxxxxxxx-xxxxxxxxxxxxxxx
>>>>>>> 62ba8270e6eebe146a04ed628942cbd304b7772a
    access_token = "xxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    try:
        # initialize the Oauth object for OAuthHandler class in tweepy module
        # parameters are consumer key, consumer_secret and callback(optional)
        oauth = OAuthHandler(consumer_key, consumer_secret)
        oauth.set_access_token(access_token, access_token_secret)
        username = OAuthHandler.get_username(oauth)
        api = API(oauth)
        yield api
        yield  username
    except TweepError:
        return 0

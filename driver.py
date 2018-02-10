from authentication import auth
from getTweets import fetch_tweets

if __name__ == '__main__':
    api_obj, usrName = auth()
    if not usrName:
        print("Invalid keys or tokens.\nAuthentication Failed!!")
    else:
        print("Logged in as:", usrName)

    tweets = fetch_tweets(api_obj)

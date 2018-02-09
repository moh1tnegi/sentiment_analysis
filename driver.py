import tweepy
import re
from textblob import TextBlob
import authentication as auth

if __name__ == '__main__':
	auth = auth.auth()
	if not auth:
		print("Invalid keys or tokens.\nAuthentication Failed!!")
	else:
		print("Username:", auth)
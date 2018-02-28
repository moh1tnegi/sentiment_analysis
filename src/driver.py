import sys
from re import sub
from textblob import TextBlob
from authentication import auth
from getTweets import fetch_tweets
from final_hit import get_em


if __name__ == '__main__':
    try:
        api_obj, usrName = auth()
        print("Logged in as:", usrName)
    except ValueError:
        print("Invalid keys or tokens.\nAuthentication Failed!!\n")
        print("Please checkout \"README.md\" and \"authentication.py\" file.")
        sys.exit()
    twat = []
    srch, tweets = fetch_tweets(api_obj)
    for strippin in tweets:
        texts = strippin.text
        anal_text = ' '.join(sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+: / / \S+)", " ", texts).split())

        bob = TextBlob(anal_text)
        textiment = {'text': texts, 'sentiment': bob.sentiment.polarity}

        if strippin.retweet_count:
            twat.append(textiment)
        else:
            if textiment not in tweets:
                twat.append(textiment)
    get_em(twat, srch)

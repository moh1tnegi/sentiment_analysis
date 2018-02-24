import re
from textblob import TextBlob
from authentication import auth
from getTweets import fetch_tweets
from final_hit import get_em


def reged_tweets(txs):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+: / / \S+)", " ", txs).split())


if __name__ == '__main__':
    api_obj, usrName = auth()
    if not usrName:
        print("Invalid keys or tokens.\nAuthentication Failed!!")
    else:
        print("Logged in as:", usrName)
    twat = []
    tweets = fetch_tweets(api_obj)
    for strippin in tweets:
        texts = strippin.text
        anal_text = reged_tweets(texts)
        bob = TextBlob(anal_text)
        tweetiment = {'text': texts, 'sentiment': bob.sentiment.polarity}

        if strippin.retweet_count:
            twat.append(tweetiment)
        else:
            if tweetiment not in tweets:
                twat.append(tweetiment)
    get_em(twat)

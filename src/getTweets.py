def fetch_tweets(api):
    search_for = 'Donald Trump'  # input('Enter username to search for: ')
    tweet_counts = 100  # int(input('Enter the number of tweets to fetch: '))

    tweets = api.search(q=search_for, counts=tweet_counts)  # status object returned
    # print(len(tweets))
    return tweets

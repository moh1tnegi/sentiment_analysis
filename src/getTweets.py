def fetch_tweets(api):
    search_for = input('Enter username to search for: ')
    tweet_counts = int(input('Enter the number of tweets to fetch: '))

    tweets = api.search(q=search_for, count=tweet_counts)  # status object returned
    yield search_for
    yield tweets

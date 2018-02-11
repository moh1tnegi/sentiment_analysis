def fetch_tweets(api):
    search_for = input('Enter a name to search for: ')
    tweet_counts = int(input('Enter the number of tweets to fetch: '))

    tweets = api.search(search_for, tweet_counts)

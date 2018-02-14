def fetch_tweets(api):
    search_for = input('Enter username to search for: ')
    tweet_counts = int(input('Enter the number of tweets to fetch: '))

    tweets = api.search(q=search_for, counts=tweet_counts)
    for i in tweets:
        print(i)

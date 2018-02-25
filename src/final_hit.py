def get_em(tweets, srch):
    pos = []
    neg = []
    nut = []

    tw_len = len(tweets)
    for a_tweet in tweets:
        if a_tweet['sentiment'] > 0:
            pos.append(a_tweet)
        elif not a_tweet['sentiment']:
            nut.append(a_tweet)
        else:
            neg.append(a_tweet)
    get_per = lambda x: (100*(len(x)))/tw_len
    print("\nSentiment Analysis for {}:".format(srch))

    print("Positive tweets: ", end=' ')
    try:
        print(get_per(pos))
    except ZeroDivisionError:
        print(0)

    print("Negative tweets: ", end=' ')
    try:
        print(get_per(neg))
    except ZeroDivisionError:
        print(0)

    print("Neutral tweets:  ", end=' ')
    try:
        print(get_per(nut))
    except ZeroDivisionError:
        print(0)

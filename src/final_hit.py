def get_em(tweets):
    pos = []
    neg = []
    nut = []

    for a_tweet in tweets:
        # print(a_tweet['sentm'])
        if a_tweet['sentiment'] == 1:
            pos.append(a_tweet)
        elif not a_tweet['sentiment']:
            nut.append(a_tweet)
        else:
            neg.append(a_tweet)
    tw_len = len(tweets)
    # p_per = (100*(len(pos)))/tw_len
    n_per = (100*(len(neg)))/tw_len
    u_per = (100*(len(nut)))/tw_len
    # print(p_per)
    print(n_per)
    print(u_per)
    # for i in tweets:
    #     print(i)

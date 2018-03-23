# turbo-broccoli
The repository is about twitter sentiment analysis which determines the opinions of people 
by analysing their tweets.

Prerequisites:
    Please make sure that python v3 is your default system python interpreter or use virtual env.

    * Get your own twitter api at https://apps.twitter.com
    * Fill the required information (you may leave boxes without (*)).
    * Get all the four keys and tokens and put 'em into 'authentication.py' source file.
    * Install pip if not pre-installed - $ apt install python3-pip
    * Install textblob                 - $ pip install textblob
    * Install tweepy                   - $ pip install tweepy
    
Simply run the command in terminal after having above packages-
    $ python driver.py

It will ask you for a username to search for. After providing it a username and number of
tweets to analyse, you will get the analysed percentage of tweets.

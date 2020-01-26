# MOSTLY NOT MADE BY ME**
# https://github.com/feconroses/gather-tweets-from-stream

import tweepy
import ssl
import time
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError
import datetime

''' More info on Standard Search API:
https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html'''

# Add your Twitter API credentials
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"

# Handling authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create a wrapper for the API provided by Twitter
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Function for handling pagination in our search
def limit_handled(cursor):
    while True:
        try:
            try:
                yield cursor.next()
            except StopIteration:
                return
        except tweepy.RateLimitError:
            print('Reached rate limit. Sleeping for >15 minutes')
            time.sleep(15 * 61)


# Function to make the search using Twitter API
def search_tweets(lang, geo):
    # Finds the tweets from cursor and iterates through
    for tweet in limit_handled(tweepy.Cursor(api.search,
                                             q="*",
                                             count=100,
                                             tweet_mode='extended',
                                             lang=lang,
                                             geocode=geo,
                                             result_type='recent',
                                             include_entities=True,
                                             until=datetime.date.today()).items(50)):

        try:

            # Checks if its an extended tweet (>140 characters)
            content = tweet.full_text

            '''Convert all named and numeric character references
            (e.g. &gt;, &#62;, &#x3e;) in the string s to the
            corresponding Unicode characters'''
            content = (content.replace('&amp;', '&').replace('&lt;', '<')
                       .replace('&gt;', '>').replace('&quot;', '"')
                       .replace('&#39;', "'").replace(';', " ")
                       .replace(r'\u', " ").replace('\u2026', "")
                       .replace('\n', ''))

            content.encode('ascii', 'ignore').decode('ascii')

            # Exclude retweets, too many mentions and too many hashtags
            if not any((('RT @' in content, 'RT' in content,
                         content.count('@') >= 2, content.count('#') >= 3))):
                file.write(content + '\n')

        except Exception as e:
            print('Encountered Exception:', e)
            pass


def work(language, geo):
    global file
    file = open('tweets.txt', 'w', encoding='utf-8')

    # Initializing the Twitter search
    try:
        search_tweets(language, geo)

    # Stop temporarily when hitting Twitter rate Limit
    except tweepy.RateLimitError:
        print("RateLimitError...waiting ~15 minutes to continue")
        time.sleep(1001)
        search_tweets(language, geo)

    # Stop temporarily when getting a timeout or connection error
    except (Timeout, ssl.SSLError, ReadTimeoutError,
            ConnectionError) as exc:
        print("Timeout/connection error...waiting ~15 minutes to continue")
        time.sleep(1001)
        search_tweets(language, geo)

    # Stop temporarily when getting other errors
    except tweepy.TweepError as e:
        if 'Failed to send request:' in e.reason:
            print("Time out error caught.")
            time.sleep(1001)
            search_tweets(language, geo)
        elif 'Too Many Requests' in e.reason:
            print("Too many requests, sleeping for 15 min")
            time.sleep(1001)
            search_tweets(language, geo)
        else:
            print(e)
            print("Other error with this user...passing")
            pass
    file.close()

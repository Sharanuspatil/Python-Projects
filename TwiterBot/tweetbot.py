import tweepy
auth = tweepy.oAuthHandler(customer_key, customer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError as e:
        time.sleep(1000)


for follower in limit_handler(tweepy.cursor(api_followers).items()):
    print(follower.name)

search_string = 'python'
numbersofTweets = 2

for tweet in limit_handler(tweepy.cursor(api.search.search_string).items(numbersofTweets)):
    try:
        tweet.favorite()
    except tweepy.TypeError as e:
        print(e.reason)
    except StopIteration:
        break

'''
Created on Feb 10, 2015

@author: hkuna
'''


import tweepy

import json

import time


CONSUMERKEY = "UAxexQi5vJav5o4S4861dw9Ew"

CONSUMER_SECRET = "0r9vvuZqCdSQE8nPchodIkN3fa5DkdV3H4dRW5Fylh1XIox4Gp"

OAUTHTOKEN = "3028284933-CtYKEYlMhmoofylwRvtdJmmicH7h75mwWoWTgbl"

OAUTHTOKENSECRET = "XGpOi7pofUkt2vJCTTwzwPE2i076KP6erzyLoWbSnGloZ"



linksFile = open('tenthousandtweetLink', 'w')

authkey = tweepy.OAuthHandler(CONSUMERKEY, CONSUMER_SECRET)  

print authkey

authkey.set_access_token(OAUTHTOKEN, OAUTHTOKENSECRET)

url_list = set()

api = tweepy.API(authkey)

search_results = tweepy.Cursor(api.search,q="http:").items()



while True:

    try:

        tweet = search_results.next()

        item= tweet._json

        eachitem={}

        tweet_created_date= item['user']['created_at']

        tweet_id= item['id_str']

        eachitem['tweetid'] = tweet_id

        eachitem['tweetcreatedDate'] = tweet_created_date

        for link in item['entities']['urls']:

            url_list.add(link['url'])

            eachitem['urllink']=link['url']
            print json.dumps(eachitem) + '\n'
            linksFile.write(json.dumps(eachitem) + '\n')

            if len(url_list) == 10000:
                break

    except tweepy.TweepError as e:
        print e
        time.sleep(60 * 2)

        continue

    except StopIteration:

        break

print len(url_list)

print url_list
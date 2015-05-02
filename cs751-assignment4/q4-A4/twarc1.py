from twarc import Twarc
import json

client_key = "UAxexQi5vJav5o4S4861dw9Ew"

client_secret = "0r9vvuZqCdSQE8nPchodIkN3fa5DkdV3H4dRW5Fylh1XIox4Gp"

access_token = "3028284933-CtYKEYlMhmoofylwRvtdJmmicH7h75mwWoWTgbl"

access_token_secret = "XGpOi7pofUkt2vJCTTwzwPE2i076KP6erzyLoWbSnGloZ"

url_list = 0;

linksFile = open('1000links-30th.txt', 'w')

t = Twarc(client_key, client_secret, access_token, access_token_secret)
for tweet in t.search("applewatch"):
    print(tweet)
    linksFile.write(json.dumps(tweet) + '\n')
    if url_list  == 1000:
       break



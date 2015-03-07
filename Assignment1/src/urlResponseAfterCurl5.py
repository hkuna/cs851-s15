'''
Created on Feb 10, 2015

@author: hkuna
'''
import requests
import json


opfile=open("6thousand.txt",'r')
allstatuscodes={}
tweetResponseFile = open('urlStatusAfterCurlCalls5', 'w')
for line in opfile:
    eachLink=json.loads(line)
    try:
        response = requests.head(eachLink['urllink'], allow_redirects=True)
        allstatuscodes['tweetcreatedDate']=eachLink['tweetcreatedDate']
        allstatuscodes['lasturl']=response.url
        arr = []
        arr.append(response.status_code)
        history = response.history
        for rs in history:
            arr.append(rs.status_code)
        allstatuscodes['statuscodes'] = arr
        tweetResponseFile.write(json.dumps(allstatuscodes) + '\n')
    except:    # This is the correct syntax
        continue
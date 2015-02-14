'''
Created on Feb 12, 2015

@author: hkuna
'''

import json


opfile=open("responseAfterCurlCallsforUniqueCount.txt",'r')
allstatuscodes={}
#tweetResponseFile = open('uniqueUrlCount.txt', 'w')
setcounter = set()
counter=0
for line in opfile:
    eachLink=json.loads(line)
    try:
        setcounter.add(eachLink['lasturl'])
        counter = counter+1
    except:    # This is the correct syntax
        continue
print counter
print len(setcounter)
duplicateCount= counter-len(setcounter)
print duplicateCount
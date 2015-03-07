import datetime
import json
import time
import statistics
from statistics import mean
from statistics import median
from statistics import stdev





opfile=open("carbondatedata",'r')
allstatuscodes={}
ageFile = open('deltaAge.txt', 'w')
statisticsFile = open('statistics.txt','w')
deltas=set()
for line in opfile:
    eachLink=json.loads(line)
    try:
        tweetdate = eachLink["tweetcreatedDate"]
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweetdate,'%a %b %d %H:%M:%S +0000 %Y'))
        ct = time.strptime(ts, "%Y-%m-%d %H:%M:%S")
        cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
        now = datetime.datetime.now()
        tweetagedays = (now - cdt).days
        
        carbondate = eachLink["urlcreatedDate"]
        ct = time.strptime(carbondate, "%Y-%m-%dT%H:%M:%S")
        cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
        now = datetime.datetime.now()
        carbonagedays = (now - cdt).days
        
        absoluteDelta= abs(tweetagedays-carbonagedays)
        print absoluteDelta
        ageFile.write(str(absoluteDelta) + '\n')
        deltas.set(absoluteDelta)
    except:    # This is the correct syntax
        continue
meandata = mean(deltas)
mediandata = median(deltas)
stddevdata = stdev(deltas)
statisticsFile.write("mean data is : "+str(meandata)+"\n")
statisticsFile.write("median data is : "+str(mediandata)+"\n")
statisticsFile.write("stddev data is : "+str(stddevdata)+"\n")



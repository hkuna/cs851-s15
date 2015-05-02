import json
import string
import subprocess
import time
f = open('urlStatusAfterCurlCalls','r+')
i=1
for line in f:
	data = json.loads(line)
	link = str(i)'.html'
	url = "http://labs.mementoweb.org/timemap/link/"+data['lasturl']
	subprocess.Popen(['wget','--output-document='+link,url])
	i=i+1
			
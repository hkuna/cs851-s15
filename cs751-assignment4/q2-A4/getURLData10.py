import json
import string
import subprocess
import time
f = open('urlStatusAfterCurlCalls9','r+')
i=9000
for line in f:
	data = json.loads(line)
	link = str(i) + '.html'
	subprocess.Popen(['wget','--output-document',link,"http://labs.mementoweb.org/timemap/link/"+str(data['finalurl'])])
	i=i+1
		
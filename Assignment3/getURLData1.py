import json
import string
import subprocess
import time
f = open('C:\\Users\\systems\\workspace\\Assignment3-cs751\\src\\assign3\\urlStatusAfterCurlCalls','r+')
i=1
for line in f:
	data = json.loads(line)
	link = str(i) +'.html'
	subprocess.Popen(['wget','--output-document',link,str(data['lasturl'])])
	i=i+1
			
import requests
import sys
import time

count = 0
for i in xrange(1, (int(sys.argv[1]) + 1)):
    r = requests.get('http://google.com')
    ts = int(time.time())
    if r.status_code == 200:
        print "Request #" + str(count) + " TS: " + str(ts) + ": " + str(r.status_code) + " " + str(r.headers)
    count += 1
    time.sleep(1)

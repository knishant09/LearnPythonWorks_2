import queue
import threading
import urllib.request


def getUrl(q, url):
    print('getUrl(' + url + ') called from a thead.')
    q.put(urllib.request.urlopen(url).read())


theurls = ["http://google.com", "http://google.de", "http://google.ca"]

threadQueue = queue.Queue()

for u in theurls:
    t = threading.Thread(target=getUrl, args=(threadQueue, u))
    t.daemon = True
    t.start()

output = threadQueue.get()
# print(output)

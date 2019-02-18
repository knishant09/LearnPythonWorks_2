import urllib3.response, urllib.request


#response = urllib.request.urlopen("https://www.journaldev.com")

#print(response.read())
url = 'https://www.journaldev.com'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

request = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(request)

print(resp.read())

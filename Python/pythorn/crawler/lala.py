import urllib.request

response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html.decode('utf-8')
print(html)

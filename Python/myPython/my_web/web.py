import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print type(res)

print res.status_code

print requests.codes.ok

print len(res.text)

print res.text
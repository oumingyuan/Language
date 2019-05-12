import requests

print requests

request = requests.get(url='http://www.itwhy.org')

print request.status_code  # 200 mean success

request1 = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})

print request1.url

print request1.text

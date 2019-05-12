import requests

r = requests.get(url='http://www.itwhy.org')
# print(r.status_code)

r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
# print(r.url)
r = requests.get('https://github.com/timeline.json')

r = requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})

print(r.url)
print(r.text)

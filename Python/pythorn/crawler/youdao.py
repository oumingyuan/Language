import urllib.request
import urllib.parse
import json



url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
data = {}

data['i'] = '我爱你'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1500205918536'
data['sign'] = '0d1639e0611bfbcda8e2cc6650cde9fe'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)

html = response.read().decode('utf-8')

target = json.loads(html)

# print('翻译结果：%' % (target['']))



print(target['translateResult'][0][0]['tgt'])

import json

print json

dict = {'a': 123, 'b': [1, 2]}

print type(dict)

d1 = json.dumps(dict)

print type(d1)

print dict
print d1

d2 = json.loads(d1)

print d2

print type(d2)

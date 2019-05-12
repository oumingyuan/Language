import json

print json
data1 = {'b': 789, 'c': 456, 'a': 123}
data2 = {'a': 123, 'b': 789, 'c': 456}

print data1 == data2

d1 = json.dumps(data1, sort_keys=True)

print type(d1)
print d1

d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys=True)

print d2
print d3

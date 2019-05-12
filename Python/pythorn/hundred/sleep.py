import time

print(time)

myD = {1: 'A', 2: 'B', 3: 'C'}

for key, value in dict.items(myD):
    print(key, value)
    time.sleep(2)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

goldTxt = open('C:/Users/oumin/Desktop/gold.txt')

listSnow = []
for line in goldTxt:
    listSnow = line.split('},{')

# print(list)

listNew = []
for element in listSnow:
    # print(element)

    ding = element.split(',')

    dictionary = dict()
    for xue in ding:
        xue1 = xue.split(':')

        if len(xue1) == 2:
            dictionary[xue1[0]] = xue1[1]

    listNew.append(dictionary)

print(listNew)

from bs4 import BeautifulSoup

print(BeautifulSoup)

soup = BeautifulSoup(open('D:/web/html/reptile/scenery.html', 'r', encoding='utf-8'), 'lxml')

print(soup)
print('===================================================================')

# print(soup.find_all('li', attrs={'nu': '3'}))

# Tags = soup.find_all('a', attrs={'class': 'price'})
# print(Tags)

# tmpTag = soup.find('li', attrs={'nu': '2'})
# print(tmpTag)
# print(tmpTag.a)

tag = soup.find('li', attrs={'nu': '4'})
tag.get('nu')
print(tag.a.get_text())

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/Users/runzhou/git/scrapy/chap2/sc_04_beautifulsoup/index.html'), 'lxml')

tag = soup.p

# 1. get attr
# print(tag)
# print(tag['class'])

# 2. get all attrs
# print(tag.attrs)

# 3. add, change, delete attrs
tag = soup.a
print("修改前tag内容与属性:")
print(tag)
print(tag.attrs)
print('\n=====================\n')

# 增加name属性
tag['name'] = 'link-name'
# 修改class属性
tag['class'] = 'brother'
# 删除id属性
del tag['id']

print('\n=====================\n')
print("修改后tag内容与属性:")
print(tag)
print(tag.attrs)

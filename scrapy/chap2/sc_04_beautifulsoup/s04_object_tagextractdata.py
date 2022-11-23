from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/Users/runzhou/git/scrapy/chap2/sc_04_beautifulsoup/index.html'), 'lxml')

# 抽取title对象
tag = soup.title
print("tag内容:")
print(tag)
print("tag名称:" + tag.name)
print('\n=====================\n')
# 更改title的name值
tag.name = 'newtitle'
print("修改后tag内容:")
print(tag)
print("修改后tag名称:" + tag.name)
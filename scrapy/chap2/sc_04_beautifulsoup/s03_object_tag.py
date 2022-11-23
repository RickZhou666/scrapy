from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/Users/runzhou/git/scrapy/chap2/sc_04_beautifulsoup/index.html'), 'lxml')

# 提取title对象
title = soup.title

# 提取a对象
a = soup.a

print(title.name)
print(a.name)
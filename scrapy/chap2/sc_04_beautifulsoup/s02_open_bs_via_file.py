from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/Users/runzhou/git/scrapy/chap2/sc_04_beautifulsoup/index.html'), 'lxml')

print(soup.prettify())

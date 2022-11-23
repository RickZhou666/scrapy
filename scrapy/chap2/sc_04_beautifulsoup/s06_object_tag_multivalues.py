from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="semantic ui"></p>', 'lxml')
print(soup.p['class'])
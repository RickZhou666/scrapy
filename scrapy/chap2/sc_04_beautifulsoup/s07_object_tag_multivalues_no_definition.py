from bs4 import BeautifulSoup

soup = BeautifulSoup('<p no-definition="semantic ui"></p>', 'lxml')
print(soup.p['no-definition'])
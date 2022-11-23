from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="page">This is a test</p>', 'lxml')
print(soup.name)

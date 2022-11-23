from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="page">This is a test</p>', 'lxml')
tag = soup.p
print(tag)
tag.string.replace_with("This is another test")
print(tag)
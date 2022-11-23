html_doc = """
<!DOCTYPE html>
<html>
<head><title>The Dormouse's story</title></head>
<body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon the time there were three little sisters;
        and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

# 1. 当作属性
print(soup.find_all(id="link1"))

print('\n================================================================================================\n')

# 2. 正则
print(soup.find_all(href=re.compile("elsie")))

print('\n================================================================================================\n')

# 3. 列表
print(soup.find_all(id=['link1', 'link3']))

print('\n================================================================================================\n')

# 4. True
print(soup.find_all(id=True))

print('\n================================================================================================\n')

# 5. HTML5 data-*

# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# print(data_soup.find_all(data-foo="value"))


print('\n================================================================================================\n')

# 6. 换成字典来搜索
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
print(data_soup.find_all(attrs={"data-foo": "value"}))

print('\n================================================================================================\n')

# 7. 搜索class时改写成class_
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.find_all('a', class_='sister'))

print('\n================================================================================================\n')

# 8. text
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=['Elsie', 'Lacie', 'Tillie']))
print(soup.find_all(text=re.compile('Dormouse')))
print(soup.find_all("a", text='Elsie'))

print('\n================================================================================================\n')
# 9. limit
print(soup.find_all('a', limit=2))

print('\n================================================================================================\n')
# 10. recursive

html_doc = """
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

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

# 1. next_element, previous_element 获得前后节点
# <head><title>The Dormouse's story</title></head>
print(soup.head.next_element)
print(soup.title.previous_element)


# 2. next_elements 和 previous_elements获得迭代器
print('\n================================================================================================\n')
for element in soup.head.next_elements:
    print(repr(element))

print('\n================================================================================================\n')

for element in soup.head.previous_elements:
    print(repr(element))

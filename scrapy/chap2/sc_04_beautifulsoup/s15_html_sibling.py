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

# 1. .next_sibling 和 .previous_sibling 查询兄弟节点
print(soup.a)
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.next_sibling.next_sibling.next_sibling)
print(soup.a.next_sibling.next_sibling.next_sibling.next_sibling)
print(soup.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)
print(soup.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)
# print(soup.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)

print('\n================================================================================================\n')

print(soup.body)
print(soup.body.previous_sibling)
print(soup.body.previous_sibling.previous_sibling)
print(soup.body.previous_sibling.previous_sibling.previous_sibling)
print(soup.body.previous_sibling.previous_sibling.previous_sibling.previous_sibling)
# print(soup.body.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling)

print('\n================================================================================================\n')

# 2. 获得所有兄弟节点
for i in soup.a.next_siblings:
    print(repr(i))
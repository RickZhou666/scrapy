html_doc = """
<!DOCTYPE html>
<html lang="en">
<head><title>The Dormouse's story</title></head>
<body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon the time there were three little sisters;
        and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

# 1. 获得所有tag
tag = soup.body
print(tag.contents)

print('\n================================================================================================\n')

# 2. 获得列表大小，通过索引取值
print(len(tag.contents))

for i in range(len(tag.contents)):
    print(i, tag.contents[i])
# print(tag.contents[0])
# print(tag.contents[1])
# print(tag.contents[5])

print('\n================================================================================================\n')
# 3. .children属性
tag = soup.body
for i in tag.children:
    print(i)


print('\n================================================================================================\n')

# 4. 只有一个子节点，或仅包含一个字符串
# <head><title>The Dormouse's story</title></head>
print(soup.title.string)
print(soup.head.string)

print('\n================================================================================================\n')

# 5. 如果有多个子节点，则无法调用.string 直接获取string
print(soup.body.string)

print('\n================================================================================================\n')

# 6. 多节点可以使用.strings循环获取内容
for string in soup.strings:
    print(repr(string))

print('\n================================================================================================\n')

# 7. stripped_strings去除换行、段首和段末的空白
for string in soup.stripped_strings:
    print(string)
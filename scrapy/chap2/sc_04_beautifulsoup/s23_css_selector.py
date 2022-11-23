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

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

# 1. 通过标签名直接查找
print(soup.select("title"))
# 通过标签逐层查找
print(soup.select("html title"))
# 查找某个tag标签下的直接子标签
print(soup.select("p > a"))

print('\n================================================================================================\n')
# 2. 通过CSS类名查找
print(soup.select(".sister"))
print(soup.select("[class~=sister]"))

print('\n================================================================================================\n')
# 3. 通过ID查找
print(soup.select("#link1"))
print(soup.select("a#link2"))

print('\n================================================================================================\n')
# 4. 通过是否存在某个属性来查找
print(soup.select("a[href]"))

print('\n================================================================================================\n')
# 5. 通过属性值来查找
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('a[href^="http://example.com/"]'))
print(soup.select('a[href$="tillie"]'))
print(soup.select('a[href*=".com/el"]'))
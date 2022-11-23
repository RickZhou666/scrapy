html_doc = """
<!DOCTYPE html>
<html lang="en">
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon the time there were three little sisters;
  and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
  and they lived at the bottom of a well.</p>

<p class="story">...</p>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')

# 1. .parent 获取父节点
# <head><title>The Dormouse's story</title></head>
title_tag = soup.title
print(title_tag)
print(title_tag.parent)

print('\n================================================================================================\n')

# 2. .parents递归获取所有的父节点
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
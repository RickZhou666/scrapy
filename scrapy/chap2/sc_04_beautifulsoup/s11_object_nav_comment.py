from bs4 import BeautifulSoup
import bs4

html_doc = "<p><!--This is a comment--></p>"
                # 不能有空格，否则识别为NoneType
html_doc = "<p><!-- This is a comment--></p>"
soup = BeautifulSoup(html_doc, 'lxml')
comment = soup.p.string

print(comment)
print(type(comment))
print(type(comment) == bs4.element.Comment)
if type(comment) == bs4.element.Comment:
    print("comment string, drop it")

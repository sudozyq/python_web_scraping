from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="html.parser")
# nameList = bsObj.find_all("span", {"class":{"green","red"}})
# allText = bsObj.findAll(id = "text")
# print(allText[0].get_text())

# nameList = bsObj.find_all(text="the prince")
# print(len(nameList))

# for name in nameList:
#     print(name)
#     print(name.get_text())
# 处理子标签
# for child in bsObj.find("table", {"id":"giftList"}).children:
#     print(child)

# 处理兄弟标签
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_silblings:
#     print(sibling)

# 父标签处理
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
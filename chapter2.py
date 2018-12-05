from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")
# nameList = bsObj.find_all("span", {"class":{"green","red"}})
allText = bsObj.findAll(id = "text")
print(allText[0].get_text())

# nameList = bsObj.find_all(text="the prince")
# print(len(nameList))

# for name in nameList:
#     print(name)
#     print(name.get_text())
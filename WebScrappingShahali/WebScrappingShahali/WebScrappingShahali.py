
import requests
from bs4 import BeautifulSoup
import module

data = dict()
request = requests.get("https://lent.az/xeber-lenti")
html_parser = BeautifulSoup(request.text,"html.parser")
for i in html_parser.find_all("div",{"class":"item_foot"}):
    url =  i.find("a",{"class":"title"}).get("href")
    print("AXTARILIR:",url)
    module.write_data(module.read_data(url))
    print(module.read_data(url))
    print("="*100)

import requests
from bs4 import BeautifulSoup

def read_data(url):
    data = dict()
    request = requests.get(url)
    html_parser = BeautifulSoup(request.text,"html.parser")
    data["XEBERIN UNVANI"] = url 
    data["XEBERIN ADI"] = html_parser.find("h1",{"class":"news_title"}).get_text()
    data["XEBERIN MEZMUNU"] = html_parser.find("div",{"class":"news_content"}).get_text()
    return data

def write_data(data):
    xeber = ""
    for l,j in data.items():
        xeber = xeber + l + "-->" + j + "\n"
    file = open("data","a",encoding="utf-8")
    file.write(xeber)
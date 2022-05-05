import requests
from bs4 import BeautifulSoup

https = "https://ute.udn.vn/LoaiBoPhan/1/Ban-Giam-hieu.aspx"
result = requests.get(https)
soup = BeautifulSoup(result.content,"html")
print(soup)
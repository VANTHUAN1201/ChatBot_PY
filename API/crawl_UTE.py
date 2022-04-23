from lxml import html
import requests
from bs4 import BeautifulSoup
import json
def crawl_data():
    sinhvienPATH = "https://ute.udn.vn/LoaiBoPhan/1/Ban-Giam-hieu.aspx"

    tree = requests.get(sinhvienPATH)
    soup = BeautifulSoup(tree.content,"html")
    result = soup.find_all("strong")
    strr = []
    for i in result:
        strr.append(i.text)
    for i in strr:
        i = str(i).replace('\xa0',' ')
    json_data = {
        "intents" : [{
            "tag": ["HIỆU TRƯỞNG"],
            "questions": ["Hiệu trưởng"],
            "answers" : []
        },
        {
            "tag": ["PHÓ HIỆU TRƯỞNG"],
            "questions": ["hiệu phó"],
            "answers" : []
        }
        ]
    }
    for i in json_data["intents"]:
        count = 0
        for j in strr:
            for k in i["tag"]:
                if k == j:
                    if i["answers"] == []:
                        i["answers"].append(strr[count+1])
                    else:
                        for ii in i["answers"]:
                            ii+=", "+strr[count+1]
            count+=1
    print(json_data)
    f = open("data/UTE.json",'w+', encoding="utf-8")
    f.write(json.dumps(json_data))
    f.close()

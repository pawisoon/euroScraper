# -*- coding:UTF-8 -*-
from lxml import html, etree
import requests, json, sys, re

requests.packages.urllib3.disable_warnings()

### Change year in URL to change data set
link = "https://www.euro-millions.com/results-archive-2021"
page = requests.get(link)
tree = html.fromstring(page.content)

archives = tree.xpath(".//*[@id=\"content\"]/div")

storage = []


def removeAllWhiteSpaces(item):
    item = item.strip()
    item = item.rstrip()
    item = item.lstrip()
    return item


for archive in archives:

    balls = archive.xpath(".//ul/li/text()")
    date = archive.xpath(".//a/text()")

    numbers = []
    stars = []
    if len(date) == 2:
        # print(str(date))
        for ball in balls[0:5]:
            numbers.append(int(ball))

        for ball in balls[5:7]:
            stars.append(int(ball))

        try:
            data = {
                "date": removeAllWhiteSpaces(date[1]),
                "normalballs": numbers,
                "stars": stars,
            }
            storage.append(data)

        except Exception:
            print("error")

o = json.dumps(storage)

with open("data_file.json", "w") as write_file:
    json.dump(storage, write_file)

print(o)

# -*- coding:UTF-8 -*-
from lxml import html, etree
import requests, json, sys, re


requests.packages.urllib3.disable_warnings()

link = "https://www.euro-millions.com/results-archive-2005"
page = requests.get(link)
tree = html.fromstring(page.content)

archives = tree.xpath(".//*[@id=\"content\"]/div")

storage = []


for archive in archives:

    balls = archive.xpath(".//ul/li/text()")
    date = archive.xpath(".//a/text()")
    plusballs = archive.xpath(".//div/ul/li/text()")

    numbers = []
    stars = []
    plusnumbers = []

    if len(date) == 1:
        # print(str(date))
        for ball in balls[0:5]:
            numbers.append(int(ball))

        for ball in balls[5:7]:
            stars.append(int(ball))

        for plusball in plusballs:
            plusnumbers.append(int(plusball))

        try:
            data = {
                "date": date,
                "normalballs": numbers,
                "stars": stars,
                "plusballs": plusnumbers
            }
            storage.append(data)

        except Exception:
            print("error")

o = json.dumps(storage)

with open("data_file.json", "w") as write_file:
    json.dump(storage, write_file)

print(o)



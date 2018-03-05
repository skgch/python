# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import csv

def get_nikkei_heikin():
    url = "http://www.nikkei.com/markets/kabu"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    nikkei_heikin = ""
    span_tags = soup.find_all("span")

    for span_tag in span_tags:
        try:
            class_ = span_tag.get("class").pop(0)
            if class_ in "mkc-stock_prices":
                nikkei_heikin = span_tag.string
                break
        except:
            pass

    return nikkei_heikin

while True:
    if datetime.now().minute != 59:
        sleep(58)
        continue
    
    with open("nikkei_heikin.csv", "a", encoding="UTF-8") as f:
        while datetime.now().second != 59:
            sleep(1)

        sleep(1)
        
        writer = csv.writer(f, lineterminator="\n")
        columns = []
        columns.append(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        columns.append(get_nikkei_heikin())
        writer.writerow(columns)
import requests
import time
from lxml import html
import pandas as pd
from pandas import DataFrame, Series

hf = []
bt = []
wz = []


def get_tiezi(n):

    cookie = {
        '你的cookie'}
    s = requests.session()
    for page in range(n):
        URL = "https://tieba.baidu.com/f?kw=双梦镇&ie=utf-8&pn=%d" % (
                page * 50)
        r = s.get(URL,cookies=cookie)
        #r.encoding = r.apparent_encoding
        tree = html.fromstring(r.text)
        #els = tree.xpath('//div[@class="threadlist_title pull_left j_th_tit "]')
        els = tree.xpath('//div[@class="t_con cleafix"]')
        for el in els:
            huifu = int(el.xpath('div[1]/span/text()')[0])
            title = str(el.xpath('div[2]/div/div[1]/a/@title')[0])
            url_ = 'https://tieba.baidu.com' + \
                el.xpath('div[2]/div/div[1]/a/@href')[0]
            #if title.find('818') > 0 or title.find('616') > 0 or title.find('树洞') > 0:
            if huifu>5000:
                hf.append(huifu)
                bt.append(title)
                wz.append(url_)
        print(page)
        time.sleep(1)

if __name__ == "__main__":
    get_tiezi(12000)
#print(hf, bt, wz)
    df = DataFrame([bt,wz,hf],
               columns=None,
               index=['标题', '网址', '回复数'])
    df = df.T
    df = df.sort_values(by='回复数')
    print(df)
    df.to_excel('热帖汇总.xls', index=False)

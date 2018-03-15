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
        'Cookie': 'BAIDUID=68BBD6BEA3FF01379004E5263D6DDFF9:FG=1; PSTM=1518656385; BIDUPSID=7983C904C7E2EF180659A2A08559ABA8; TIEBA_USERTYPE=04e88654f6f16f46b0a22c1e; TIEBAUID=cee2d6fef653b91a6fd71b99; bottleBubble=1; rpln_guide=1; baidu_broswer_setup_éªèå¨å¿=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; FP_UID=0976f5408754b7679e681c71e9c98f31; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[abe9uUBlp-C]=mk3SLVN4HKm; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1519357453,1519607415,1519614430,1519619255; 41379149_FRSVideoUploadTip=1; H_PS_PSSID=1421_25548_21126_17001_20927; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1519621449; BDUSS=EYxTFVzcGUtZFVTeTdacnZZQXpGM3FhUk1zMU9SOUs0QTl4NUhxdldPNVpJcnRhQVFBQUFBJCQAAAAAAAAAAAEAAABNZXcC0anI2tTa0MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFmVk1pZlZNaZ; STOKEN=586796bea86a25d4dd1e70e03d979a58e53353855ca7a78cbf637b547d5dbe78'}
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

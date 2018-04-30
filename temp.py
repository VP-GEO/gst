# moduulit joita prosessi tällä hetkellä käyttää -> jatkossa luultavasti Scrapy
import requests
from lxml import html

link_collection = []

# haetaan esim 100 sivua artikkeleita jotka sisältävät hakusanan
for i in range(1, 101):
    url = "https://asia.nikkei.com/search/find?search_keyword=HAKUSANA&page=" + str(i)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    
    # polku otsikon hypertekstiin
    a = tree.xpath('//div[@class="article-box"]//h2/a/@href')
    
    link_collection.append(a)

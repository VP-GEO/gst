import requests
from lxml import html

link_path = open("filepath")
read_links = link_path.read()
linklist = read_links.split(",")

base_url = "https://asia.nikkei.com"
full_url = []

for i in linklist:
    url = base_url + i
    full_url.append(url)

read_body = []

# otetaan pelkkä body text jokaisen otsikon takaa löytyvästä artikkelista
for i in full_url:
    page = requests.get(i)
    tree = html.fromstring(page.content)
    body_class = tree.xpath('//div[@class="articleBodyText"]//p/text()')
    read_body.append(body_class)

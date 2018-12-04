# IMPORTS FOR SRAPING TECHCRUNCH
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# SCRAPE FUNCTION
def scrape(src, page):
    post_links = []
    post_title = []
    post_auth = []
    post_desc = []
    post_time = []
    post_img = []
    url = "https://techcrunch.com/"+src+"/page/"+page
    print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    a_tags = soup.find_all('a')
    div_tags = soup.find_all('div')
    span_tags = soup.find_all('span')
    figure = soup.find_all("figure", {"class": "post-block__media"})
    time_tag = soup.find_all('time')

    # FETCH POST TIME
    for t in time_tag:
        content = re.sub('\s+', ' ', str(t.text))
        content = content.strip()
        post_time.append(content)

    # FETCH POST IMG
    for f in figure:
        img = f.find('img')
        h = img.get('src')
        post_img.append(h)

#     # FETCHES POST AUTHORS
    for s in span_tags:
        c = s.get('class')
        if(type(c) == type(post_links)):
            for i in c:
                if(i == "river-byline__authors"):
                    span_inner = s.find('a')
                    content = span_inner.text
                    content = re.sub('\s+', ' ', content)
                    content = content.strip()
                    post_auth.append(content)

    # FETCHES POST DESCRIPTION
    for d in div_tags:
        c = d.get("class")
        if(type(c) == type(post_links)):
            for i in c:
                if(i == "post-block__content"):
                    content = d.text
                    content = re.sub('\s+', ' ', content)
                    content = content.strip()
                    content = content+"...."
                    post_desc.append(content)

    # FETCHES POST LINK AND TITLE
    for a in a_tags:
        c = a.get("class")
        if(type(c) == type(post_links)):
            for i in c:
                if(i == "post-block__title__link"):
                    post_links.append(a.get("href"))
                    content = str(re.sub("<.*?>", "", str(a)))
                    content = re.sub('\s+', ' ', content)
                    content = content.strip()
                    post_title.append(content)

    data_dict = {}
    data = []
    print(str(len(post_title))+" post_title Fetched")
    print(str(len(post_desc))+" post_desc Fetched")
    print(str(len(post_auth))+" post_auth Fetched")
    print(str(len(post_links))+" post_links Fetched")
    print(str(len(post_img))+" post_img Fetched")
    print(str(len(post_time))+" post_time Fetched")

    # POPULATING FETCHED DATA TO JSON OBJECT
    for i in range(len(post_links)):
        if i>(len(post_title)-1):
            post_title.append(" ")
        if i>(len(post_desc)-1):
           post_desc.append(" ")
        if i>(len(post_auth)-1):
            post_auth.append(" ")
        if i>(len(post_links)-1):
           post_links.append(" ")
        if i>(len(post_img)-1):
            post_img.append(" ")
        if i>(len(post_time)-1):
            post_time.append(" ")
        data_dict = {
            "post_title": post_title[i],
            "post_desc": post_desc[i],
            "post_auth": post_auth[i],
            "post_links": post_links[i],
            "post_img": post_img[i],
            "post_time": post_time[i]
        }
        data.append(data_dict)
    return data

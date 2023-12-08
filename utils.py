from requests_html import HTMLSession
import requests_html as rh
import re

def get_links(name, page):
    rs = set()
    paragraphs = page.html.find('p')

    for p in paragraphs:
        for l in p.links:
            if not re.match("/wiki/", l) or re.match("/wiki/.*[/?].*", l) or re.match("/wiki/[(Help)(Catagory)(Template)].*", l):
                continue
            hash_loc = l.find('#')
            if hash_loc > -1:
                rs.add(l[6:hash_loc])
            else:
                rs.add(l[6:])
    return rs

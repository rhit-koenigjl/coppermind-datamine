from requests_html import HTMLSession
import re

def get_links(name, session):
    rl = []
    r = session.get('https://coppermind.net/wiki/' + name)
    ls = r.html.links
    for l in ls:
        if not re.match("/wiki/", l):
            continue
        if re.match("/wiki/.*[:/%?].*", l):
            continue
        rl.append(l[6:])
    return rl

class Connection: 
    def __init__(self, from_page, to_page) -> None:
        self.from_page = from_page
        self.to_page = to_page

class Chain:
    def __init__(self) -> None:
        self.start = None
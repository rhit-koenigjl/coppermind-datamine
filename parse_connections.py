from requests_html import HTMLSession
from utils import get_links
from termcolor import cprint
import os

if os.path.exists('connections.txt'):
    os.remove('connections.txt')
connection_f = open("connections.txt", "x")

STARTING_LINK = 'Coppermind:Welcome'
session = HTMLSession()

visited_pages = []
to_visit = [STARTING_LINK]
visited_page = 0

while len(to_visit) > 0:
    current_loc = to_visit.pop(0)
    visited_page += 1
    print("Page " + str(visited_page) + '/' + str(len(to_visit)))
    cprint(current_loc, "blue")

    visited_pages.append(current_loc)
    links = get_links(current_loc, session)

    for l in links:
        connection_f.write(current_loc + '->' + l + '\n')
        if l in to_visit:
            continue
        if l not in visited_pages:
            to_visit.append(l)
    input("continue?")

connection_f.close()




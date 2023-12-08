from requests_html import HTMLSession
from utils import get_links
from termcolor import cprint
import os
import time

def create_connections():
    # Constants
    CONNECTIONS_PATH = 'connections.txt'
    PAGES_PATH = 'pages.txt'
    WIKI_PATH = 'https://coppermind.net/wiki/'
    STARTING_LINK = input('Starting Link: ')

    # Handle files
    if os.path.exists(CONNECTIONS_PATH):
        os.remove(CONNECTIONS_PATH)
    connection_f = open(CONNECTIONS_PATH, "x")

    if os.path.exists(PAGES_PATH):
        os.remove(PAGES_PATH)
    pages_f = open(PAGES_PATH, "x")

    # Starts the HTML Session that will be passed to the web-crawler
    session = HTMLSession()

    # Data for the crawler to avoid duplocates and track progress, using a stack to avoid memory reallocation... not sure if python cares or not
    to_visit = [STARTING_LINK]
    visited_pages = set()
    visited_page = 0

    while len(to_visit) > 0:
        current_loc = to_visit.pop()
        visited_page += 1
        print("Page " + str(visited_page) + '/' + str(len(to_visit)))
        cprint(current_loc, "blue")

        visited_pages.add(current_loc)
        page = session.get(WIKI_PATH + current_loc)
        links = get_links(current_loc, session)

        # Probably more efficient ways to do this here. Sample size seems small enough that it shouldn't matter
        for l in links:
            connection_f.write(current_loc + '->' + l + '\n')
            if l in to_visit:
                continue
            if l not in visited_pages:
                to_visit.add(l)
        time.sleep(5)

    # Closing files
    connection_f.close()
    pages_f.close()



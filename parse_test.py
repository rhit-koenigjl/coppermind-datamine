from requests_html import HTMLSession
from utils import get_links
from termcolor import cprint
import os

if os.path.exists('test.txt'):
    os.remove('test.txt')
test_f = open(r"test.txt", "x")

STARTING_LINK = '/wiki/Hoid'
session = HTMLSession()

visited_pages = []
to_visit = [STARTING_LINK]
visited_page = 0

links = get_links(STARTING_LINK, session)
for l in links:
    test_f.write(l + '\n')

test_f.close()
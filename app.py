from requests_html import HTMLSession
from termcolor import cprint
from random import choice
from utils import get_links
import re

session = HTMLSession()

starting_name = '/wiki/' + input("Name of starting article:")
cur_loc = starting_name
crawl_length = int(input("Number of movements: "))

for i in range(crawl_length):
    links = get_links(cur_loc, session)
    new_loc = choice(links)
    cprint(cur_loc + ' -> ' + new_loc, "light_green")
    cur_loc = new_loc

print("final article: " + cur_loc)

import inquirer
import os
from utils import get_links
from requests_html import HTMLSession
from parse_connections import create_connections

command_question = [
    inquirer.List('action',
        message="Actions:",
        choices=['Get Page Links', 'Send Discord Message'],
    ),
]

command = inquirer.prompt(command_question)

com = command['action']
if com == 'Get Page Links':
    search_page = input('source page: ')
    session = HTMLSession().get(f'https://coppermind.net/wiki/{search_page}')
    links = get_links(search_page, session)
    print(links)
elif com == 'Send Discord Message':
    print('Unimplimented action')
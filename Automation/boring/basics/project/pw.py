#! /urs/bin/env python3
# py.py - An insecure password locker program

PASSWORDS = {'email': 'Fuwe7SGIKc81eejQ71VULsd982wj8H',
             'blog': 'Vmief8liwef932rILOh7DS382lkhds',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passwords for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)


import random as r

with open('./wordlists/firstnames.txt', 'r') as file:
    firstnames = file.read().split('\n')
with open('./wordlists/lastnames.txt', 'r') as file:
    lastnames = file.read().split('\n')

def generateName():
    name = f'{r.choice(firstnames)} {r.choice(lastnames)}'
    return name
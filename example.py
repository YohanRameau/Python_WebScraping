import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/'

response = requests.get(url)
''' Normalement response retourne code 200 
print(response) '''

#response.ok renvoie un booleen en fonction de la reponse obtenu.
if response.ok:
    ''' response.text retourne tout le code html de la page.
    print(response.text) '''
    links = list()
    soup = BeautifulSoup(response.text, 'lxml')
    tds = soup.findAll('td')
    for td in tds:
        a = td.find('a')
        link = a['href']
        links.append(url + link)
    print(links)
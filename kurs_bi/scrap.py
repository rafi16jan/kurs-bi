import requests
try:
   from bs4 import BeautifulSoup
except:
   import subprocess
   subprocess.call(['python', __file__.replace('scrap', 'install')])
   from install import main as install_pip
   install_pip()
   from bs4 import BeautifulSoup

def parse():
    url = "http://www.bi.go.id/id/moneter/informasi-kurs/transaksi-bi"
    page = requests.get(url).text
    soup = BeautifulSoup(page)
    currencies = []
    kurs = {}
    table = soup.find('table', attrs={'class': 'table1'})
    #table_body = table.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns:
           columns = [element.text.strip() for element in columns]
           currencies += [(columns[0], columns[0])]
           kurs.update({columns[0]: {'nilai': float(columns[1].replace(',', '')), 'kurs_jual': float(columns[2].replace(',', '')), 'kurs_beli': float(columns[3].replace(',', ''))}})
    return currencies, kurs

data = parse()
currencies = data[0]
kurs = data[1]

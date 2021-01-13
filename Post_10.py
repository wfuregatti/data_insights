from bs4 import BeautifulSoup
import requests

url = "https://www.x-rates.com/calculator/?from=CAD&to=USD&amount=1/"
req = requests.get(url)

soup = BeautifulSoup(req.content,'html.parser')
exrate = soup.find(attrs={'class': 'ccOutputRslt'})

print(exrate.text)
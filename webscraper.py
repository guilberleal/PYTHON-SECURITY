
import string
from bs4 import BeautifulSoup
import requests
site = requests.get("http://www.climatempo.com.br/").content #recebe conteudo da requisicao do http do site

soup = BeautifulSoup(site,"html.parser") #objeto soup baixando do site o html


temperatura = soup.find()
 
print(temperatura)



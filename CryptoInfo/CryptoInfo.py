from bs4 import BeautifulSoup
import requests

def searchCourse(Name):
    SoupPage = requests.get(page + cryptoName)
    soup = BeautifulSoup(SoupPage.content, 'html.parser')
    error = soup.find_all("div", {"class": "title-404"})
    if error:
        print("Diese Währung existiert nicht. ")
    else:
        soup.prettify()
        result = soup.select_one("span[class*=text-large2]").text
        print("Die Währung " + Name + " hat einen Kurs von " + result + " USD \n \n \n")








while True:
    cryptoName = input("Geben Sie den Namen der Cryptocurrency ein.")
    cryptoName = cryptoName.lower()
    cryptoName = cryptoName.replace(' ', '-')
    page = "https://coinmarketcap.com/currencies/"
    searchCourse(cryptoName)




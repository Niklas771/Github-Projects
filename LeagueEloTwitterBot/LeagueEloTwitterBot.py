from bs4 import BeautifulSoup
import urllib
import time
import tweepy as tp

def get_Elo():

    page_name = 'http://euw.op.gg/summoner/userName=varg+koala'

    page = urllib.urlopen(page_name)

    soup = BeautifulSoup(page, "html.parser")

    elo = soup.select_one("span[class*=tierRank]").text

    return elo

def tweet():

    # Benutzerdaten
    consumer_key = 	'Jxnkp8o7xCyQapoDSOBs6TX7D'
    consumer_secret = '7HykhhSzLGpztN5HaOdcT9bpVTu529zyRenbqN2Y82AbLUah2m'
    access_token = 	'958744586746322945-2PqPC9k7L1uEpO09qd6kVYp9GG2XSNr'
    access_secret = '4D0ruBUijq5j7Ah8hPEAJpqsWgfkCmmuBepW17u7E5Vpo'

    # Twitter-Login
    auth = tp.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api = tp.API(auth)

    #Tweet
    current_elo = get_Elo()
    Message = "VarG Koala is currently ranked " + current_elo
    api.update_status(Message)


while True:
    tweet()
    time.sleep(10800)







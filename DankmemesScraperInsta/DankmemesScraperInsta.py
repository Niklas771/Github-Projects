import praw
import urllib
import time
from InstagramAPI import InstagramAPI
from PIL import Image
import numpy as np

#Scraped die Titel der 10 "hottesten" Posts und speichert sie in einem Array.
def getTitles():
    count = 1
    titles = list()
    for submission in reddit.subreddit('dankmemes').hot(limit=7):
        if count > 1:
            titles.append(submission.title)
        count += 1
    return titles


#Scraped die Link zu den Bildern der 10 "hottesten" Posts und speichert sie in einem Array.
def getImages():
    count = 1
    images = list()
    for submission in reddit.subreddit('dankmemes').hot(limit=7):
        if count > 1:
            images.append(submission.url)
        count += 1
    return images



def ReadyImages(imageX):
    path = "/root/DankmemesScraperInsta/MemeImages"

    for image in imageX:
        imageTitle = image.split('/', 3)[3]
        urllib.urlretrieve(image, path + imageTitle)




def PostOnInstagram(titleX):
    InstaAPI = InstagramAPI("Benutzername", "Passwort")
    InstaAPI.login()

    photo_path = "/root/DankmemesScraperInsta/MemeImages/test.jpg"
    caption = titleX + " #dankmemes #memes #meme #dank #dankmeme #funny #reddit"

    InstaAPI.uploadPhoto(photo_path, caption=caption)



def resizeTest(imageX):
    im = Image.open('/root/DankmemesScraperInsta/MemeImages' + imageX)
    sqrWidth = np.ceil(np.sqrt(im.size[0] * im.size[1])).astype(int)
    im_resize = im.resize((sqrWidth, sqrWidth))
    im_resize.save('/root/DankmemesScraperInsta/MemeImages/test.jpg')

#Konfiguriert die Verbindung zu Reddit
reddit = praw.Reddit(client_id="2-H-w5AGA0AjoQ",
                         client_secret="x7dApme7diAblQ5dmE0AIcyNKlo",
                         user_agent="DankmemesScraper")


while True:
    titles = getTitles()
    images = getImages()
    time.sleep(10)
    ReadyImages(images)

    for image,title in zip(images,titles):
        Newimage = image.split('/', 3)[3]
        resizeTest(Newimage)
        time.sleep(10)
        PostOnInstagram(title)
        time.sleep(14400)

import requests
from bs4 import BeautifulSoup
import os

src = []
url = input('Введите ссылку ')

def createFolder(name: str):
    try:
        folder = os.mkdir(name)
    except OSError:
        print ("Создать директорию %s не удалось" % name)
    else:
        print ("Успешно создана директория %s " % name)
    return folder

def download(src: list, folder: str)-> None:
    index = 0
   
    for url in src:
        path = folder + '\\' + str(index) + '.png'
        r = requests.get(url)
        with open(path, 'bw') as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        index+=1 

def get_html(url:str) -> str:
    request = requests.get(url)
    return request.text

def parse(url: str) -> None:
    soup = BeautifulSoup(get_html('https://www.yakaboo.ua/'+ url))

    div = soup.find('ul', {'class': 'media-content__list list_fragments'})
    imgs = div.find_all('img')
    for img in imgs:
        src.append(img.get('data-original'))

parse(url)
url = 'C:\\Users\Z580\\Desktop\\Страницы книги\\' + url.split('.')[0]
createFolder(url)
download(src, url)

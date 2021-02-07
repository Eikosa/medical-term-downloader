# -*- coding: utf-8 -*-
url='https://saglik.sozlugu.org/random-ajax/'
import urllib.request
from bs4 import BeautifulSoup
import time
import random
import os

toplam=0
i=0
bulunamamaAdedi=0
while True:
    if bulunamamaAdedi>40:
        break
    i+=1
    a=time.time()
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page.read(), 'html.parser')

    yazi=soup.text.replace("Ã§","ç").replace(",\n",", ")
    yazi=yazi.strip()[:-1].strip().capitalize()
    baslik=yazi.split("\n")[0]
    dizin="Kelimeler\\"+baslik.capitalize().replace("/","")+".txt"
    
    if not os.path.isfile(dizin):
        print(f"{baslik}\ntoplam: {i}, süre: {round(toplam,2)}, ortalama: {round(toplam/i,2)}, bulunamama: {bulunamamaAdedi}")
        bulunamamaAdedi=0

        text_file = open(dizin, "w",encoding="UTF-8")
        text_file.write(yazi)
        text_file.close()
        #print("-"*10+"\n")
        
        time.sleep(random.uniform(0,1))
    else:
        print(baslik,"zaten var.")
        bulunamamaAdedi+=1
    toplam+=time.time()-a
print("Bu iş bu kadar mı?")

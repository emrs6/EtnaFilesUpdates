# coding: utf-8
import requests
from bs4 import BeautifulSoup

URL = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari/bursa-akaryakit-fiyatlari"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

# Yeþil kutudaki deðeri almak için ilgili HTML elementini ve sýnýfýný belirtmelisiniz.
# Bu örnekte tam olarak hangi sýnýfý veya elementi seçmeniz gerektiðini bilemiyorum.
# Bu nedenle genel bir yaklaþým sunuyorum.
degerler = soup.find_all("span", class_="with-tax")
ikinci_deger = degerler[57].text

print(ikinci_deger)
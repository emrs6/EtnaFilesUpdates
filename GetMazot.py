# coding: utf-8
import requests
from bs4 import BeautifulSoup

URL = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari/bursa-akaryakit-fiyatlari"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

# Ye�il kutudaki de�eri almak i�in ilgili HTML elementini ve s�n�f�n� belirtmelisiniz.
# Bu �rnekte tam olarak hangi s�n�f� veya elementi se�meniz gerekti�ini bilemiyorum.
# Bu nedenle genel bir yakla��m sunuyorum.
degerler = soup.find_all("span", class_="with-tax")
ikinci_deger = degerler[57].text

print(ikinci_deger)
import requests
from bs4 import BeautifulSoup

# İnternet bağlantısını kontrol etmek için bir URL kullanabiliriz.
# Örneğin, Google'ın anasayfasını kontrol etmek için kullanabiliriz.
test_url = "https://www.google.com"

# İnternet bağlantısı yoksa bu fonksiyon bağlantı hatası döndürecek
def check_internet_connection(url):
    try:
        requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        return False

# İnternet bağlantısı kontrol ediliyor
internet_connection = check_internet_connection(test_url)

if internet_connection:
    # İnternet bağlantısı varsa, veri çekmeye devam edebiliriz
    URL = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari/bursa-akaryakit-fiyatlari"
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")

    # Yeşil kutudaki değeri almak için ilgili HTML elementini ve sınıfını belirtmelisiniz.
    # Bu örnekte tam olarak hangi sınıfı veya elementi seçmeniz gerektiğini bilemiyorum.
    # Bu nedenle genel bir yaklaşım sunuyorum.
    degerler = soup.find_all("span", class_="with-tax")
    ikinci_deger = degerler[57].text

    print(ikinci_deger)
else:
    # İnternet bağlantısı yoksa 0 değerini veriyoruz
    print("0")

# version: 1.0.3
import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.petrolofisi.com.tr/Fuel/Search"
HEADERS = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":    "https://www.petrolofisi.com.tr",
    "Referer":   "https://www.petrolofisi.com.tr/akaryakit-fiyatlari",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    ),
    "X-Requested-With": "XMLHttpRequest",
}

def fetch_html(city_id, district_id):
    payload = {
        "template":   "1",
        "cityId":     str(city_id).zfill(2),
        "districtId": str(district_id).zfill(5),
    }
    r = requests.post(URL, headers=HEADERS, data=payload)
    r.raise_for_status()
    return r.text

def get_diesel_price(html, district_id="01612"):
    soup = BeautifulSoup(html, "html.parser")
    # Orhangazi satırını seçiyoruz
    tr = soup.find("tr", {"data-disctrict-id": district_id})
    if not tr:
        raise RuntimeError("Orhangazi satırı bulunamadı.")
    # Başlıklar ve hücreler
    headers = [th.get_text(strip=True) for th in soup.select("table thead th")]
    cells   = [td.get_text(strip=True) for td in tr.find_all("td")]

    # “Diesel” başlıklı sütunu bul
    for h, c in zip(headers, cells):
        if "diesel" in h.lower():
            # Ondalıklı sayıları ayıkla
            nums = re.findall(r"\d+\.\d{2}", c)
            if not nums:
                raise RuntimeError("Dizel fiyatı metninde sayı bulunamadı.")
            # İlk sayıyı alıyoruz
            return nums[0]
    raise RuntimeError("Dizel sütunu bulunamadı.")

def check_internet_connection(url):
    try:
        requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        return False

if __name__ == "__main__":
    # İnternet bağlantısını kontrol et
    test_url = "https://www.google.com"
    internet_connection = check_internet_connection(test_url)
    if not internet_connection:
        print("internet yok")
        exit(1)
    # 1) Bursa için önce tüm ilçeleri çek (districtId=01600)
    html = fetch_html(city_id=16, district_id=1600)
    # 2) HTML'i kullanarak dizel fiyatını al
    price = get_diesel_price(html, district_id="01612")
    print(price)

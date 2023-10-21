# -*- coding: utf-8 -*-
import pandas as pd
import json
import sys
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os

def load_data(kaydet_path):
    with open(kaydet_path, "r", encoding="utf-8") as f:
        ayarlar = json.load(f)

    # Veriler DataFrame'ini oluşturma
    veriler_df = pd.DataFrame(ayarlar)


    return veriler_df

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def save_to_excel(df, columns, suggested_filename):
    root = tk.Tk()
    root.withdraw()  # Arka planda çalışmasını sağlar

    # Bugünün tarihini al
    

    # Kullanıcının "Masaüstü" klasörünü bul
    documents_path = os.path.expanduser('~/Desktop')


    # Dosya seçim dialogunu aç
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                                             initialdir=documents_path,  # Dosya dialogunun açılacağı başlangıç klasörü
                                             initialfile=suggested_filename)  # Önerilen dosya adı


    # Eğer bir dosya seçildiyse kaydet
    if file_path:
        df[columns].to_excel(file_path, index=False, engine='openpyxl')
        print(f"Excel dosyası {file_path} olarak kaydedildi.")

def main():
    if len(sys.argv) != 3:
        print("Kullanım: python jsontoexcel.py <kaydet.json yolu> <sütun adları>")
        return

    

    # Dosya yollarını ve sütun adlarını oku
    kaydet_path = sys.argv[1]
    columns = [col.strip() for col in sys.argv[2].split(',')]
    df = load_data(kaydet_path)
    
    # İlk satırdaki "Mazot" ve "Ton" değerlerini al
    mazot_fiyati = df.iloc[0]["MazotD"]
    # Bugünün tarihini al
    today = datetime.today().strftime('%Y-%m-%d')

    # "MazotD" sütununu listeden çıkar
    columns.remove("MazotD")

    # Önerilen dosya adını oluştur
    suggested_filename = f"{mazot_fiyati:.0f} TL {today} Fiyat Listesi.xlsx"

    save_to_excel(df, columns, suggested_filename)

    print(f"Excel dosyası olarak kaydedildi.")

if __name__ == "__main__":
    main()

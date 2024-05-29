from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

def main():
    try:
        print("")
        print("*"*170)
        print("")

        personel1 = Personel(1, "Melisa", "Demir", "Temizlik", 17000)
        personel2 = Personel(2, "Ekrem", "Bağcı", "Güvenlik", 20000)
        print(personel1)
        print(personel2)
        print("")

        doktor1 = Doktor(3, "Bülent", "Kara", "Doktor", 60500, "Çocuk Doktoru", 20, "Medipol")
        doktor2 = Doktor(4, "Selin", "Şekerci", "Doktor", 47000, "Kardiyoloji", 9, "Medipol")
        doktor3 = Doktor(5, "Samet", "Yılmaz", "Doktor", 63000, "Nöroloji", 21, "Şifa")
        print(doktor1)
        print(doktor2)
        print(doktor3)
        print("")

        hemsire1 = Hemsire(6, "Kerem", "Öncü", "Hemşire", 40000, "08.00-16.00", "Yoğun Bakım Hemşireliği", "Sada")
        hemsire2 = Hemsire(7, "Zeynep", "Bilge", "Hemşire", 42000, "20.00-08.00", "Ameliyathane Hemşireliği", "Medipol")
        hemsire3 = Hemsire(8, "Yağmur", "Taş", "Hemşire", 43000, "16.00-24.00", "Çocuk Acil Bakım Hemşireliği", "Şifa")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)
        print("")

        hasta1 = Hasta(9, "İrem", "Selim", "2003/12/07", "Ağrı", "İlaç Tedavisi")
        hasta2 = Hasta(10, "Sıla", "Ekran", "1985/01/24", "Çatlak", "Alçı Tedavisi")
        hasta3 = Hasta(11, "Mert", "Demir", "2000/10/12", "Kırık", "Alçı Tedavisi")
        print(hasta1)
        print(hasta2)
        print(hasta3)

        print("")
        print("*"*170)
        print("")

        data = [
                [1, "Melisa", "Demir", "Temizlik", 17000, None, None, None, None, None, None, None, None, None],
                [2, "Ekrem", "Bağcı", "Güvenlik", 20000, None, None, None, None, None, None, None, None, None],
                [3, "Bülent", "Kara", "Doktor", 60500, "Çocuk Doktoru", 20, "Medipol", None, None, None, None, None, None],
                [4, "Selin", "Şekerci", "Doktor", 47000, "Kardiyoloji", 9, "Medipol", None, None, None, None, None, None],
                [5, "Samet", "Yılmaz", "Doktor", 63000, "Nöroloji", 21, "Şifa", None, None, None, None, None, None],
                [6, "Kerem", "Öncü", "Hemşire", 40000, None, None, "Sada", "08.00-16.00", "Yoğun Bakım Hemşireliği", None, None, None, None],
                [7, "Zeynep", "Bilge", "Hemşire", 42000, None, None, "Medipol", "20.00-08.00", "Ameliyathane Hemşireliği", None, None, None, None],
                [8, "Yağmur", "Taş", "Hemşire", 43000, None, None, "Şifa", "16.00-24.00", "Çocuk Acil Bakım Hemşireliği", None, None, None, None],
                [9, "İrem", "Selim", None, None, None, None, None, None, None, 9, "2003/12/07", "Ağrı", "İlaç Tedavisi"],
                [10, "Sıla", "Ekran", None, None, None, None, None, None, None, 10, "1985/01/24", "Çatlak", "Alçı Tedavisi"],
                [11, "Mert", "Demir", None, None, None, None, None, None, None, 11, "2000/10/12", "Kırık", "Alçı Tedavisi"]
                ]
        
        df = pd.DataFrame(data, columns = ["NO", "AD", "SOYAD", "DEPARTMAN", "MAAŞ", "UZMANLIK", "DENEYİM-YILI", "HASTANE", "ÇALIŞMA SAATİ",
                                           "SERTİFİKA", "HASTA-NO", "DOĞUM-TARİHİ", "HASTALIK", "TEDAVİ"], index=["","","","","","","","","","",""])
        
        df_filled = df.fillna(0)  # Eksik verileri 0 ile doldurma
        print(df_filled)
        print("")
        print("*"*170)

        print("\nDOKTORLARIN UZMANLIK ALANLARI VE TOPLAM SAYISI:\n")
        doktorlar = df[df["DEPARTMAN"] == "Doktor"]
        uzmanlik_alanlari = doktorlar.groupby("UZMANLIK").size().reset_index(name="SAYI")
        print(uzmanlik_alanlari)
        print("")
        print("*"*170)

        deneyim = doktorlar[doktorlar["DENEYİM-YILI"] > 5]
        deneyim = deneyim.shape[0]
        print(f"\n5 YILDAN FAZLA DENEYİME SAHİP DOKTORLARIN SAYISI: {deneyim}\n")
        print("*"*170)

        hasta_bilgileri = df_filled[df_filled["DEPARTMAN"] == 0]
        hasta_bilgileri2 = hasta_bilgileri.sort_values(by="AD")
        print("\nHASTA ADINA GÖRE SIRALANMIŞ DATAFRAME:\n")
        print(hasta_bilgileri2)
        print("")
        print("*" * 170)

        print("\nMAAŞI 7000 TL'NİN ÜZERİNDE OLAN PERSONELLER:\n")
        maas_bilgisi = df[df["MAAŞ"] > 7000][["NO", "AD", "SOYAD", "DEPARTMAN", "MAAŞ"]]
        print(maas_bilgisi)
        print("")
        print("*"*170)

        df_filled["DOĞUM-TARİHİ"] = pd.to_datetime(df_filled["DOĞUM-TARİHİ"], errors='coerce', format='%Y/%m/%d')
        dogum_tarihi_1990_sonrasi = df_filled[df_filled["DOĞUM-TARİHİ"].dt.year >= 1990]
        print("\nDOĞUM TARİHİ 1990 VE SONRASI OLAN HASTALAR:\n")
        print(dogum_tarihi_1990_sonrasi)
        print("")
        print("*"*170)

        yeni_df = df[["AD", "SOYAD", "DEPARTMAN", "MAAŞ", "UZMANLIK", "DENEYİM-YILI", "HASTALIK", "TEDAVİ"]]
        df_filled2 = yeni_df.fillna(0)
        print("\nYENİ DATAFRAME\n")
        print(df_filled2)
        print("")
        print("*"*170)

    except Exception as e:
        print(f"Hata: {e}")
    
if __name__ == "__main__":
    main()



    






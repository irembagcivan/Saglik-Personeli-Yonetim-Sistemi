from Personel import Personel # Personel modülünden Personel sınıfı çağırılır
from Doktor import Doktor # Doktor modülünden Doktor sınıfı çağırılır
from Hemsire import Hemsire # Hemsire modülünden Hemsire sınıfı çağırılır
from Hasta import Hasta # Hasta modülünden Hasta sınıfı çağırılır
import pandas as pd # Pandas kütüphanesi pd takma adıyla eklenir

def main():
    try: # Kodun içinde hata yakalama bloğu oluşturur.
        print("")
        print("*"*170)
        print("")
        # Personel sınıfı için 2 nesne oluşturuldu.
        personel1 = Personel(1, "Melisa", "Demir", "Temizlik", 17000) 
        personel2 = Personel(2, "Ekrem", "Bağcı", "Güvenlik", 20000)
        print(personel1)
        print(personel2)
        print("")
        # Doktor sınıfı için 3 nesne oluşturuldu.
        doktor1 = Doktor(3, "Bülent", "Kara", "Doktor", 60500, "Çocuk Doktoru", 20, "Medipol")
        doktor2 = Doktor(4, "Selin", "Şekerci", "Doktor", 47000, "Kardiyoloji", 9, "Medipol")
        doktor3 = Doktor(5, "Samet", "Yılmaz", "Doktor", 63000, "Nöroloji", 21, "Şifa")
        print(doktor1)
        print(doktor2)
        print(doktor3)
        print("")
        # Hemşire sınıfı için 3 nesne oluşturuldu.
        hemsire1 = Hemsire(6, "Kerem", "Öncü", "Hemşire", 40000, "08.00-16.00", "Yoğun Bakım Hemşireliği", "Sada")
        hemsire2 = Hemsire(7, "Zeynep", "Bilge", "Hemşire", 42000, "20.00-08.00", "Ameliyathane Hemşireliği", "Medipol")
        hemsire3 = Hemsire(8, "Yağmur", "Taş", "Hemşire", 43000, "16.00-24.00", "Çocuk Acil Bakım Hemşireliği", "Şifa")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)
        print("")
        # Hasta sınıfı için 3 nesne oluşturuldu.
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
        
        # Pandas DataFrame oluşturuldu. Satır ve sütun adları belirlendi.
        df = pd.DataFrame(data, columns = ["NO", "AD", "SOYAD", "DEPARTMAN", "MAAŞ", "UZMANLIK", "DENEYİM-YILI", "HASTANE", "ÇALIŞMA SAATİ",
                                           "SERTİFİKA", "HASTA-NO", "DOĞUM-TARİHİ", "HASTALIK", "TEDAVİ"], index=["","","","","","","","","","",""])
       
        
        df_filled = df.fillna(0)  # Boş olan değişken değerlerine 0 atandı
        print(df_filled) # DataFrame' i yazdırma işlemi
        print("")
        print("*"*170)
        
        # Doktorların uzmanlık alanlarına göre gruplandırılması ve her bir gruptaki toplam doktor sayısını yazdırma
        print("\nDOKTORLARIN UZMANLIK ALANLARI VE TOPLAM SAYISI:\n")
        doktorlar = df[df["DEPARTMAN"] == "Doktor"] # DataFrame'den departmanı "Doktor" olan satırları seçer
        uzmanlik_alanlari = doktorlar.groupby("UZMANLIK").size().reset_index(name="SAYI") 
        print(uzmanlik_alanlari)
        print("")
        print("*"*170)
        '''
        groupby(): doktorlar DataFrame'ini "UZMANLIK" sütununa göre gruplar. 
        size(): Gruplandırılmış verilerin her bir grubundaki öğe sayısını hesaplar. Gruplandırılmış veri ile ilgili bir seri döndürür. 
        reset_index(name="SAYI"): Seriyi bir DataFrame'e dönüştürür ve sayıları "SAYI" adlı bir sütun olarak adlandırır. '''
        
        # 5 yıldan fazla deneyime sahip doktorların sayısını yazdırma
        deneyim = doktorlar[doktorlar["DENEYİM-YILI"] > 5] # 5 yıldan fazla deneyime sahip doktorları seçer.
        deneyim = deneyim.shape[0] # deneyim DataFrame'inin satır sayısını döndürür. 
        print(f"\n5 YILDAN FAZLA DENEYİME SAHİP DOKTORLARIN SAYISI: {deneyim}\n")
        print("*"*170)
        ''' doktorlar["DENEYİM-YILI"] > 5 : doktorlar DataFrame'inin "DENEYİM-YILI" sütunundaki
        her bir değerin 5 den büyük olup olmadığına bakar. Boolean döndürür.'''
        
        # Hastaları isimlerine göre alfabetik olarak sıralama
        hasta_bilgileri = df_filled[df_filled["DEPARTMAN"] == 0] # Departmanı olmayan (yani hasta olan) satırları seçer.
        hasta_bilgileri2 = hasta_bilgileri.sort_values(by="AD") # Bu satırları hasta isimlerine göre sıralar.
        print("\nHASTA ADINA GÖRE SIRALANMIŞ DATAFRAME:\n")
        print(hasta_bilgileri2)
        print("")
        print("*" * 170)
        '''sortvalues(): hasta_bilgileri DataFrame'indeki satırları "AD" sütunundaki değerlere göre alfabetik olarak sıralar. 
        sort_values metodu, bir DataFrame'in belirli bir sütununa göre sıralanmasını sağlar.'''

        #  Maaşı 7000 TL'nin üzerinde olan personelleri yazdırma
        print("\nMAAŞI 7000 TL'NİN ÜZERİNDE OLAN PERSONELLER:\n")
        maas_bilgisi = df[df["MAAŞ"] > 7000][["NO", "AD", "SOYAD", "DEPARTMAN", "MAAŞ"]] # Maaşı 7000 TL'nin üzerinde olan personelleri seçer ve sadece belirli sütunları alır.
        print(maas_bilgisi)
        print("")
        print("*"*170)

        # Doğum tarihi 1990 ve sonrası olan hastaları yazdırma
        df_filled["DOĞUM-TARİHİ"] = pd.to_datetime(df_filled["DOĞUM-TARİHİ"], errors='coerce', format='%Y/%m/%d') # DOĞUM-TARİHİ sütununu datetime formatına çevirir.
        dogum_tarihi_1990_sonrasi = df_filled[df_filled["DOĞUM-TARİHİ"].dt.year >= 1990] # Doğum tarihi 1990 ve sonrası olan hastaları seçer.
        print("\nDOĞUM TARİHİ 1990 VE SONRASI OLAN HASTALAR:\n")
        print(dogum_tarihi_1990_sonrasi)
        print("")
        print("*"*170)

        # Belirtilen sütunları seçerek yeni bir DataFrame oluşturulur
        yeni_df = df[["AD", "SOYAD", "DEPARTMAN", "MAAŞ", "UZMANLIK", "DENEYİM-YILI", "HASTALIK", "TEDAVİ"]]
        df_filled2 = yeni_df.fillna(0)
        print("\nYENİ DATAFRAME\n")
        print(df_filled2)
        print("")
        print("*"*170)
        
    # Hata yakalama bloğu
    except Exception as e:
        print(f"Hata: {e}")
    
if __name__ == "__main__":
    main()



    






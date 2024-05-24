from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
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

        hasta1 = Hasta(9, "İrem", "Selim", "07/12/2003", "Ağrı", "İlaç Tedavisi")
        hasta2 = Hasta(10, "Sıla", "Ekran", "24/01/1995", "Çatlak", "Alçı Tedavisi")
        hasta3 = Hasta(11, "Mert", "Demir", "12/10/2000", "Kırık", "Alçı Tedavisi")
        print(hasta1)
        print(hasta2)
        print(hasta3)
        print("")

    except Exception as e:
        print(f"Hata: {e}")
    
if __name__ == "__main__":
    main()



    






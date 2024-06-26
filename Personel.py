class Personel():
    def __init__(self, personel_no, ad, soyad, departman, maas): # Kurucu metod
        # Private değişkenler
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman 
        self.__maas = maas
    
    # Setter metotları sınıf özniteliklerini değiştirmek için kullanır
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no
    
    def set_ad(self, ad):
        self.__ad = ad
    
    def set_soyad(self, soyad):
        self.__soyad = soyad
    
    def set_departman(self,departman):
        self.__departman = departman
    
    def set_maas(self, maas):
        self.__maas = maas
    
    # Getter metotları sınıf özniteliklerini geri döndürmek için kullanılır
    def get_personel_no(self):
        return self.__personel_no
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_departman(self):
        return self.__departman
    
    def get_maas(self):
        return self.__maas
    
    # Personel bilgileri döndürülür
    def __str__(self):
        return f"Personel No:{self.__personel_no}\tAd:{self.__ad}\tSoyad:{self.__soyad}\tDepartman:{self.__departman}\tMaas:{self.__maas}TL\t"
        

    


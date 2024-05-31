from Personel import Personel # Personel modülünden Personel sınıfı çağırılır.

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas) # Kalıtım 
        # Private değişkenler
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    # Setter metotları sınıf özniteliklerini değiştirmek için kullanır
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati
    
    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika
    
    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Getter metotları sınıf özniteliklerini geri döndürmek için kullanılır
    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    # Maaş arttırma metodu
    def maas_arttir(self):
        yeni_maas = (self.get_maas() * 0.4) + self.get_maas()
        self.set_maas(yeni_maas)
    
    # Hemşire bilgileri döndürülür
    def __str__(self):
        return super().__str__() + f"Çalışma Saati:{self.__calisma_saati}\tSertifika:{self.__sertifika}\tHastane:{self.__hastane}\t"
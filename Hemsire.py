from Personel import Personel
class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati
    
    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika
    
    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    def __str__(self):
        return super().__str__() + f"Çalışma Saati:{self.__calisma_saati}\tSertifika:{self.__sertifika}\tHastane:{self.__hastane}\t"
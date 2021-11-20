#Marisa Naofa
#200511074
# Karyawan 1 TIF

class limas():
    def __init__(self):
        self.__lebaralas = None
        self.__tsegitiga = None
        self.__tlimas = None

        
    # Atribut lebaralas
    @property
    def lebaralas(self):
        return self.__lebaralas

    @lebaralas.setter
    def lebaralas(self, value):
        self.__lebaralas = value

    # Atribut tsegitiga
    @property
    def tsegitiga(self):
        return self.__tsegitiga

    @tsegitiga.setter
    def tsegitiga(self, value):
        self.__tsegitiga = value
    
    # Atribut tlimas
    @property
    def tlimas(self):
        return self.__tlimas

    @tlimas.setter
    def tlimas(self, value):
        self.__tlimas = value

    #perhitungan
    def volume(self):
        luasAlas = self.__lebaralas * self.__lebaralas
        volume = (1/3) * luasAlas * self.__tlimas
        return volume

    def luas(self):
        luas = (4 * ((1/2) * self.__lebaralas * self.tsegitiga)) + (self.__lebaralas * self.__lebaralas)
        return luas


LIMAS = limas()
PANJANG_ALAS = int(input("Masukan Nilai Panjang Alas : "))
LEBAR_ALAS = int(input("Masukan Nilai Lebar Alas : "))
TINGGI_SEGITIGA = int(input("Masukan Nilai Tinggi Segitiga : "))
TINGGI_LIMAS = int(input("Masukan Nilai Tinggi Limas : "))

LIMAS.lebaralas = PANJANG_ALAS
LIMAS.lebaralas = LEBAR_ALAS
LIMAS.tsegitiga = TINGGI_SEGITIGA
LIMAS.tlimas = TINGGI_LIMAS

VOLUME = LIMAS.volume()
LUAS = LIMAS.luas()

print("Program Hitung Volume dan Luas Limas persegi")
print("Panjang Alas :",PANJANG_ALAS)
print("Lebar Alas : ",LEBAR_ALAS)
print("Tinggi Segitiga : ",TINGGI_SEGITIGA)
print("Tinggi Limas : ",TINGGI_LIMAS)
print("===== Hasil Perhitungan =====")
print("Volume Limas Persegi : ",VOLUME,"cm3")
print("Luas Limas Persegi : ",LUAS,"cm2")
#Marisa Naofa
#200511074
# Karyawan 1 TIF


class Nilai:
    def __init__(self):
        self.__khd = None
        self.__tugas = None
        self.__uts = None
        self.__uas = None
        self.__na = None

    # Atribut khd
    @property
    def khd(self):
        return self.__khd

    @khd.setter
    def khd(self, value):
        self.__khd = value

    #Atribut tugas
    @property
    def tugas(self):
        return self.__tugas

    @tugas.setter
    def tugas(self, value):
        self.__tugas = value


    #Atribut uts
    @property
    def uts(self, value):
        return self.__uts

    @uts.setter
    def uts(self, value):
        self.__uts = value

    #Atribut uas
    @property
    def uas(self, value):
        return self.__uas

    @uas.setter
    def uas(self, value):
        self.__uas = value
    
    #Metode
    def Nilaiakhir(self):
        self.__na = (0.1 * self.__khd) + (0.2 * self.__tugas) + (0.3 * self.__uts) + (0.4 * self.__uas)
        return self.__na

    def Nilaimutu(self):
        if(self.__na>=85):
            mutu = "A"
        elif(self.__na>=75):
            mutu = "B"
        elif(self.__na>=55):
            mutu = "C"
        elif(self.__na>=40):
            mutu = "D"
        else:
            mutu = "E"
        return mutu
    

A = Nilai()
kehadiran = float(input("Masukan nilai kehadiran :"))
tugas = float(input("Masukan nilai tugas :"))
uts = float(input("Masukan nilai UTS :"))
uas = float(input("Masukan nilai UAS :"))
A.khd = kehadiran
A.tugas = tugas
A.uts = uas
A.uas = uas
nilai_akhir = A.Nilaiakhir()
mutu = A.Nilaimutu()

print("Nilai Kehadiran : ", str(kehadiran))
print("Nilai Tugas :", str(tugas))
print("Nilai UTS :", str(uts))
print("Nilai UAS :", str(uas))

print("Nilai Akhir :", str(nilai_akhir))
print("Nilai mutu :", mutu)

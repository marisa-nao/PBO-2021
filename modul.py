#Marisa Naofa
#200511074
# Karyawan 1 TIF

def Nilaiakhir(khd, tugas, uts, uas):
    nilai_akhir = (0.1 * khd) + (0.2 * tugas) + (0.3 * uts) + (0.4 * uas)
    return nilai_akhir

def Nilaimutu(nilai):
    if(nilai>=85):
        mutu="A"
    elif(nilai>=75):
        mutu="B"
    elif(nilai>=55):
        mutu="C"
    elif(nilai>=40):
        mutu="D"
    else:
        mutu="E"
    return mutu


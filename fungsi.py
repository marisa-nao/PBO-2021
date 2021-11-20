#Marisa Naofa
#200511074
# Karyawan 1 TIF

def nilaiakhir(khd, tugas, uts, uas):
    na = (0.1 * float(khd)) + (0.2 * float(tugas)) + (0.3 * float(uts)) + (0.4 * float(uas))
    return na

def nilaimutu(nilai):
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

khd = input("Masukan nilai kehadiran :")
tugas = input("Masukan nilai tugas :")
uts = input("Masukan nilai UTS :")
uas = input("Masukan nilai UAS :")
nilai_akhir = nilaiakhir(khd, tugas, uts, uas)

print("Nilai Kehadiran : ", khd)
print("Nilai Tugas :", tugas)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Akhir :", nilai_akhir)

mutu = nilaimutu(nilai_akhir)
print("Nilai mutu :", mutu)

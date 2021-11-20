#Marisa Naofa
#200511074
# Karyawan 1 TIF

from modul import *

khd = float(input("Masukan nilai kehadiran :"))
tugas = float(input("Masukan nilai tugas :"))
uts = float(input("Masukan nilai UTS :"))
uas = float(input("Masukan nilai UAS :"))

nilai_akhir = Nilaiakhir(khd, tugas, uts, uas)
mutu = Nilaimutu(nilai_akhir)

print("Nilai Kehadiran : ", khd)
print("Nilai Tugas :", tugas)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Akhir :", nilai_akhir)

mutu = Nilaimutu(nilai_akhir)
print("Nilai mutu :", mutu)
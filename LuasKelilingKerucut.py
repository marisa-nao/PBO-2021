## PROGRAM MENGHITUNG VOLUME DAN LUAS KERUCUT
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA
import math

print("====== Program Volume & Luas Kerucut ======")

#Variabel yang diperlukan :
jari2 = int(input("Masukkan jari-jari alas (Cm) : "))
tinggi = int(input("Masukkan panjang tinggi (cm) : "))
 
#Proses Penghitungan :
phi = 22/7

#Mencari garis pelukis :
pelukis = math.sqrt((jari2 * jari2) + (tinggi * tinggi))

# Menghitung luas dan volume :
luas = int(phi * jari2 * (jari2 + pelukis))
volume = int((1/3) * phi * (jari2 * jari2) * tinggi)


print("Volume Kerucut : ",round(volume,1),"Cm3")
print("Luas Kerucut : ",round(luas,1),"Cm2")

print("====== Program Selesai ======")



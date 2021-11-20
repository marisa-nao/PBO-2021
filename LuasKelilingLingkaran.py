## PROGRAM MENGHITUNG VOLUME DAN LUAS KERUCUT
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA

print("====== Program Keliling & Luas Lingkaran ======")

#Variabel yang diperlukan 
diameter = int(input("Masukan diameter lingkaran (cm) : "))

#Proses Hitung

jari = diameter/2
keliling = (22/7) * jari 
luas = (22/7) * 2 * jari

print("Keliling Lingkaran : ",round(keliling,1),"Cm")
print("Luas Lingkaran : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")

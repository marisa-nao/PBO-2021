## PROGRAM MENGHITUNG VOLUME DAN LUAS TABUNG
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA

print("====== Program Volume & Luas Tabung ======")

## Variabel yang diperlukan 
jari = int(input("Masukan Jari Jari Tabung (cm) : "))
tinggi = int(input("Masukan Tinggi Tabung (cm) : "))

#Proses Hitung Luas || rumus Luas = 2 x π x r x (r + t)
phi = (22/7)
luas = 2 * phi * jari * (jari + tinggi)

#Proses Hitung Volume || rumus Volume = π x r2 x t
volume = phi * jari * jari * tinggi

print("Volume Tabung : ",round(volume,1),"cm3")
print("Luas Tabung : ",round(luas,1),"cm2")

print("====== Program Selesai ======")

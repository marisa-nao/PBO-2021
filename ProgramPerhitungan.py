## PROGRAM BODY MAX INDEX
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA

import math


def persegi():
    print("\n\n====== Program Keliling & Luas Persegi ======")

    #Variabel yang diperlukan
    sisi = int(input("Masukan Panjang sisi (cm) : "))

    #Proses Hitung
    keliling = 4 * sisi
    luas = sisi * sisi

    print("Keliling Persegi : ",keliling,"Cm")
    print("Luas Persegi : ",luas,"Cm2")
    print("====== Program Selesai ======\n")

def segitiga():
    print("\n\n====== Program Keliling & Luas Segitiga ======")
    print("Pilih Opsi : \n1. Keliling Segitiga. \n2. Luas Segitiga")
    opsi = int(input("Masukan Pilihan (1/2) : "))

    # jika yang diketahui sisi1, sisi2 & sisi3
    if opsi == 1 :
        sisi1 = int(input("Masukan Sisi 1 (cm): "))
        sisi2 = int(input("Masukan Sisi 2 (cm): "))
        sisi3 = int(input("Masukan Sisi 3 (cm): "))
        
        #Proses Hitung
        keliling = sisi1 * sisi2 * sisi3
        print("Keliling Segitiga : ",keliling,"Cm")

        print("====== Program Selesai ======\n")

    # jika yang diketahui alas dan tinggi
    elif opsi == 2 : 
        alas = int(input("Masukan Alas Segitiga (cm) : "))
        tinggi = int(input("Masukan Tinggi Segitiga (cm) : "))

        #Proses Hitung
        luas = 0.5 * alas * tinggi
        print("Luas Segitiga : ",luas,"Cm2")
        print("====== Program Selesai ======\n\n")

    else:
        print("Pilihan tidak diketahui")
        print("====== Program Selesai =====\n")


def lingkaran ():
    print("\n\n====== Program Keliling & Luas Lingkaran ======")
    #Variabel yang diperlukan 
    diameter = int(input("Masukan diameter lingkaran (cm) : "))

    #Proses Hitung

    jari = diameter/2
    keliling = (22/7) * jari 
    luas = (22/7) * 2 * jari

    print("Keliling Lingkaran : ",round(keliling,1),"Cm")
    print("Luas Lingkaran : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======")


def balok():
    print("n\n\====== Program Keliling & Luas Balok ======")

    #Variabel yang diperlukan 
    diameter = int(input("Masukan diameter Balok (cm) : "))

    #Proses Hitung
    jari = diameter/2
    keliling = (22/7) * jari 
    luas = (22/7) * 2 * jari

    print("Keliling Balok : ",round(keliling,1),"Cm")
    print("Luas Balok : ",round(luas,1),"Cm2")

    print("====== Program Selesai ======\n")



def kerucut():
    print("n\n\====== Program Volume & Luas Kerucut ======")

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

    print("====== Program Selesai ======\n")


def bola():
    print("\n\n====== Program Volume & Luas Bola ======")

    # #Variabel yang di perlukan 
    jari = int(input("Masukan Jari Jari (cm) : "))

    #Proses Hitung Luas || rumus Luas = 4 x π x r2
    luas = 4 * (22/7) * (jari**2)

    #Proses Hitung Volume || rumus Volume = 4/3 x π x r3
    volume = 4/3 * ((22/7) * (jari**3))

    print("Volume Bola : ",round(volume,1),"cm3")
    print("Luas Bola : ",round(luas,1),"cm2")

    print("====== Program Selesai ======\n")


def tabung():
    print("\n\n====== Program Volume & Luas Tabung ======")

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

    print("====== Program Selesai ======\n")

def BMI():        
    print("\n\n== PROGRAM BODY MAX INDEX ==")

    berat = int(input("Berat Badan (Kg) : "))
    tinggi = int(input("Tinggi Badan (Cm) : "))

    # Rumus Body Max Index (Berat Badan / tinggi * Tinggi)
    ideal = berat / ((tinggi/100) * (tinggi/100))

    if ideal < 18.5 :
        print("Berat badan kurang")
    elif ideal >= 18.5 and ideal <= 24.9 :
        print("Berat Badan Normal/Ideal")
    elif ideal >= 25 and ideal <= 29.9 :
        print("Berat Badan Berlebihan/Kecenderungan Obesitas")
    elif ideal >= 30 :
        print("Obesitas")

        print("====== Program Selesai ======\n")

def menu(): 
    print("\n")
    print("----- PILIH PERHITUNGAN -----")
    print("[1] Luas & Keliling Persegi")
    print("[2] Luas & Keliling Segitiga Sama Sisi")
    print("[3] Luas & Keliling Lingkaran")
    print("[4] Volume & Luas Permukaan Balok")
    print("[5] Volume & Luas Permukaan Kerucut")
    print("[6] Volume & Luas Permukaan Bola")
    print("[7] Volume & Luas Permukaan Tabung")
    print("[8] Body Mass Index (BMI)")
    print("[0] Exit!")

    pilih = input("Pilih Nomor Perhitungan > ")

    if pilih == '1':
        persegi()
    elif pilih == '2':
        segitiga()
    elif pilih == '3':
        lingkaran()
    elif pilih == '4':
        balok()
    elif pilih == '5':
        kerucut()
    elif pilih == '6':
        bola()
    elif pilih == '7':
        tabung()
    elif pilih == '8':
        BMI()
    elif pilih == '0':
        exit()
    else:
        print("Input Tidak Diketahui!.")

if __name__ == '__main__':
    menu()


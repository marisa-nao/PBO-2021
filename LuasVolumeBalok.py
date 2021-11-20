## PROGRAM MENGHITUNG VOLUME DAN LUAS BALOK
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA

def lanjut():
    ket = ''
    nomor = 0;
    while(nomor == 0):
        ket = input("Ingin Melakukan Perhitungan Lagi (y/n) : ")
        if(ket == 'y' or ket == 'n'):
            nomor = 1
        else:
            print("Input Tidak Dikenal!")
            nomor = 0

    if ket == 'y':
        LANJUT = True
    elif ket == 'n':
        LANJUT = False
        exit()

lanjut()
        
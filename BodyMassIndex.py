## PROGRAM BODY MAX INDEX
## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA


print("== PROGRAM BODY MAX INDEX ==")

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

print = ("== PROGRAM SELESAI ==")
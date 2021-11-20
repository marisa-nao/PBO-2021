## PROGRAM MENGHITUNG NILAI FAKTORIAL

## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA

print("======== Program Menghitung Nilai Faktorial=======")

#Meminta user memasukkan nilai bilangan
n = int(input("Masukan Nilai n : "))

faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print(f'!{n} = {faktorial}')
print("===== Program Selesai =====")
# Marisa Naofa
# 200511074
# K1 TIF

print("======== Program Data Mahasiswa yang Mengikuti PKL =======")
#Tentukan jumlah data
jumlahdata = input ("Masukkan Banyak data mahasiswa:")

# Menyiapkan List kosong
mydata = []
print("=================== \n ")
#Buka sebuah file
file = open("newpkl.txt", "a")


#Counter awal
i = 1
#Pengulangan untuk Entry data
while(i <= int(jumlahdata)):
    # Input data
    print("mahasiswa ke-" + str(i))
    nama = input("Masukkan Nama Mahasiswa :")
    pkl = input("Masukkan tempat PKL yang diikuti :")

    #Tambahkan data ke dalam List
    mydata.append([nama, pkl])
    #Counter ditambah 1
    i += 1
 
for x in mydata:
     file.writelines("\n" + x[0] + " || " + x[1] )

file.close()
print(" \n ===== Berhasil Menambahkan Data Mahasiswa ====== \n ")

print("===== Menampilkan Data Mahasiswa========")

#Membaca file dData pada txt
newfile = open("newpkl.txt", "r")
print(newfile.read())
file.close()
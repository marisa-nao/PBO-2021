"""Membuat Aplikasi Menyimpan Data Buku
Menggunakan (Fungsi)"""

#Variabel global untuk menyiapkan data buku
buku = []

#fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELLUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[{}]] {}" % (indeks, buku[indeks]))

#Fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul buku: ")
    buku.append(buku_baru)

#Fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks.len(buku)):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] =judul_baru

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = input("inputkan ID buku: ")
    if(indeks >= len(buku)):
        print("ID Salah")
    else:
        buku.remove(buku[indeks])

def show_menu():
    print("\n ============== MENU =================")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit!")

    menu = input("PILIH MENU> \n")
    
    if menu == '1':
        show_data()
    elif menu == '2':
        insert_data()
    elif menu == '3':
        edit_data()
    elif menu == '4':
        delete_data()
    elif menu == '5':
        exit()
    else:
        print("Salah Pilih")



if __name__ == "__main__":
    show_menu()
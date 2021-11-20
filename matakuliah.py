#Marisa Naofa
#200511074
# Karyawan 1 TIF

NEXT = True
print ("==== Program Mata Kuliah ====")
MATAKULIAH = []
g = 1


def addData():
    matkul = input("Masukkan Nama Mata Kuliah ke-{} : ".format(g))
    MATAKULIAH.append(matkul)



def next():
    i = 0
    j = ''
    while(i == 0):
        j = input("Tambah Mata Kuliah Lagi (y/n) ? ")
        if(j == 'y' or j == 'n'):
            i = 1
        else:
            i = 0
            print("Input tidak dikenal!")
    if(j == 'y'):
        return True
    elif(j == 'n'):
        tampil()
        return False


def tampil():
    print("=" * 15)
    print("Kamu memiliki {} MK".format(len(MATAKULIAH)))
    for x in MATAKULIAH:
        print("[{}]".format(x))



while(NEXT == True):
    addData()
    g += 1
    NEXT = next()


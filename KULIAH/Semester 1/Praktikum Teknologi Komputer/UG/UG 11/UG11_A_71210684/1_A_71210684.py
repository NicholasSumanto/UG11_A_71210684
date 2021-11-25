#Operasi
def tambah(A, B):
    return A + B

def kurang(A, B):
    return A - B

def kali(A, B):
    return A * B

def bagi(A, B):
    return A / B

def pangkat(A, B):
    return A ** B
#Menampilkan Menu
def calculator():
    print("=" * 8, "Calculator Sederhana", "=" * 8)
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
#User Input
    menu = int(input("Masukan pilihan :"))
    A = int(input("Masukan bilangan 1:"))
    B = int(input("Masukan bilangan 2:"))
#Perhitungan
    if menu == 1:
        print("Hasilnya: ", tambah(A, B))
    elif menu == 2:
        print("Hasilnya: ", kurang(A,B))
    elif menu == 3:
        print("Hasilnya: ", kali(A,B))
    elif menu == 4:
        print("Hasilnya: ", bagi(A, B))
    elif menu == 5:
        print("Hasilnya: ", pangkat(A, B))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

calculator()
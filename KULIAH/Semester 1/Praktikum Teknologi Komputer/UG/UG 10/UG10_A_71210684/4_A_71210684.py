A=input("Masukkan artikel yang ingin dipindai: ")
B=input("Masukkan nama klub favorit anda: ")
C=input("Masukkan skor yang ingin dicari: ")
if  B and C in A:
    print("Hasil pencarian di temukan")
elif B in A :
    print("Hanya", B ,"yang ditemukan pada artikel ini")
elif C in A :
    print("Hanya", C ,"yang di temukan pada artikel ini")
else:
    print("Hasil pencarian", B ,"dan", C ,"tidak ditemukan")



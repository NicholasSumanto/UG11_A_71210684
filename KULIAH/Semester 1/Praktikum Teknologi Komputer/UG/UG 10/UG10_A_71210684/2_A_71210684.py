print("#"*28)
print("Kalkulator Advance Sederhana")
print("#"*28)
print("1. Menghitung sisa hasil bagi antara dua bilangan")
print("2. Menghitung hasil bagi antara dua bilangan")
print("3. Menghitung akar kubik sebuah bilangan")
menu=float(input("masukan menu yang anda pilih: "))
if menu==1 :
    bil = float(input("Masukan bilangan yang ingin dibagi: "))
    mod = float(input("Masukkan bilangan pembagi: "))
    H1 = float(bil % mod)
    print("sisa hasil bagi",bil,"dibagi dengan",mod,"adalah",H1)
elif menu==2 :
    bil = float(input("Masukan bilangan yang ingin dibagi: "))
    mod = float(input("Masukkan bilangan pembagi: "))
    H2 = float(bil // mod)
    print("hasil pembagian", bil, "dibagi dengan", mod, "dibulatkan kebawah adalah", H2)
elif menu==3 :
    bil = float(input("Masukan bilangan yang ingin dicari akar kubiknya: "))
    H3 = float(bil**(1/3))
    print("akar kubik dari",bil,"adalah",H3)
else:
    print("Menu yang anda pilih tidak tersedia")






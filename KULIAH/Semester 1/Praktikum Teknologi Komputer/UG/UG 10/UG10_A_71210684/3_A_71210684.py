A=str(input("Mendatar/Menurun?:"))
if A== "Mendatar":
    B = int(input("Masukan kolom; "))
    print("#"*B)
elif A== "Menurun":
    B = int(input("Masukan baris: "))
    row="#\n"
    print(row*B)
else:
    print("Pola tidak dikenali")



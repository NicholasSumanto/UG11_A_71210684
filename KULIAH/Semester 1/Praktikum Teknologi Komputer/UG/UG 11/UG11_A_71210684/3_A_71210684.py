def hitung_hapus():
  kalimat = input("Masukan Kalimat :")
  start = int(input("Index start :"))
  stop = int(input("Index stop :"))

  jumlah_data = str(len(kalimat))
  temp = kalimat[start-1:stop]
  hapus = str(len(temp))
  hasil = (int(hapus)/int(jumlah_data))*100
  return hasil

print(hitung_hapus())





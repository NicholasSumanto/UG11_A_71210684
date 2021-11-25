def ambil_huruf(huruf,index=0):
  panjang = str(len(huruf))
  if (int(panjang)%2) == 0:
    panjang = int(panjang)/2
    panjang = int(panjang)
    return(huruf[panjang+index])
  else:
    panjang = int(panjang)/2
    panjang = int(panjang)
    return(huruf[panjang+index])


print(ambil_huruf("abcdefg",1))
print(ambil_huruf("abcdefg",2))
print(ambil_huruf("abcd"))






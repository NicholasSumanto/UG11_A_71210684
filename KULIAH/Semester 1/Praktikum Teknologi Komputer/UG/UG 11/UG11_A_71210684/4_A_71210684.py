def ambildanbalik(huruf,start,stop,check):
  jumlah_data = str(len(huruf))
  temp = huruf[start-1:stop]
  if check:
    temp = temp[::-1]


  return temp

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
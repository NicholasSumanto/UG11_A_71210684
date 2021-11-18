rata=float(input("Masukkan nilai rata-rata UG anda: "))
TTS=float(input("Masukan nilai TTS anda: "))
TTA=float(input("Masukan nilai TAS anda: "))
print ("="*25)
R=(0.7*rata)
T=(0.15*TTS)
A=(0.15*TTA)
N=(R+T+A)
print ("Nilai anda: ",N)
if N >= 85 :
    print ("Nilai huruf anda:  A")
elif N >= 80 :
    print("Nilai huruf anda:  A-")
elif N >= 75 :
    print("Nilai huruf anda:  B+")
elif N >= 70 :
    print("Nilai huruf anda:  B")
elif N >= 65 :
    print("Nilai huruf anda:  B-")
elif N >= 60 :
    print("Nilai huruf anda:  C+")
elif N >= 55 :
    print("Nilai huruf anda:  C")
elif N >= 45 :
    print("Nilai huruf anda:  D")
else:
    print("Nilai huruf anda:  E")



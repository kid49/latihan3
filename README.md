#latihan3

Tugas latihan1.
1. Pertama kita masukan codingan untuk mencari bilangan random ::

2.Masukan codingannya seperti dibawah ini dengan benar,

###
import random

jumlah = int(input("Masukan Nilai N :"))
for i in range(jumlah):
        i=random.uniform(0.0,0.5)
        print("Masukan data : 1 =>",i)

jawab ="betul"
hitung = 0
while(jawab):
        hitung +=1
        jawab =input("sudah cukup? : ")
        if jawab == 'tidak':
                break
print ("total perulangan :" +str(hitung))
print("Selesai")
print("Tutorial by : BayuPM")
print("Copyright 2019 @bayupm")
###

Setelah itu Jalankan Runtimenya..

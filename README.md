_#latihan3
--------------------------------------------------------------------------------------------------------------------
**Mencari bilangan Random yang bersifat N : 5**
--------------------------------------------------------------------------------------------------------------------

**
**Seperti ini algoritmanya**

1. _import random_ :: Untuk mengambil bilangan random,
2. _N = int(input("Masukan nilai N : "))_ // menangkap variabel dengan huruf N, dan mendata untuk integer
3. _for x in range(n)_  // melooping sebuah bilang x dengan variabel yg sudah ada
4. _b = random.uniform(0.0,0.5)_  // membuat bilangan random yang menghasilkan 0.0 s/d 0.5
5. _print ("Data ke : ",a,"==>",b)_ ,, print data ke : a = index looping b = angka random yang sudah di buat varibelnya
6. _print("Selesai")_ // membuat kata akhir setelah dikerjakan yang akan muncul " Hasil"
7. _while jawab == "lanjutkan"_ // itu menandakan bahwa perulangan terjadi
8._ Hitung +=1 // itu mengubah atau menambahkan dari bilangan hitung = 0
9. _if jawab == "lanjuttkan"_ : // hanya jika menjawab bilangan
10. **_break_** // untuk berrhenti jika ada syntax yang ia berikan.

-Codingan

```
 print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
    print(' ')
    import random
    N = int(input("Masukan nilai N : "))
    a = 0
    for x in range(N):
        a += 1
        b = random.uniform(.0,.5)
        print('Data ke:',a,'==>',b)
    print('Selesai')
    print('')
    jawab = 'lanjutkan'
    hitung = 0
    while jawab == "lanjutkan":
        hitung += 1
        jawab = input('Ingin Mengulang? (yes/no) : ')
        if jawab == "Lanjutkan":
            break
    print('Total perulangan : ' + str (hitung))

```
<img width="274" alt="hasilgmbr1" src="https://user-images.githubusercontent.com/44864015/53164266-64c55800-3602-11e9-820b-1238f9d0ce89.PNG">

--------------------------------------------------------------------------------------------------------------------
**Mencari bilangan Random, yang terhenti jika ketik angka 0**
--------------------------------------------------------------------------------------------------------------------
-Algoritma 

1.  _Max = 0_ // variabel akhir random 0
2.  _While True_ // Perulangan Jika Benar
3. _a = int(input("Masukan bilangan"))_ // untuk mengambil data dari integer dalam input yang akan dirandom 
4. _if max <a_ // jika si max lebih kecil dari a ia akan berhenti
5. _if a ==0:_ // jika a == 0 dia berhenti memanggil
6. _break_ // jika sudah dipanggil ia akan berhenti
7. _print('bilangan paling besar : ',max)_

- Codingan

```
print("Mencari bilangan Random, yang terhenti jika ketik angka 0")
max = 0
while True :
  a = int(input("Masukan bilangan"))
  if max < a :
     max = a
  if a ==0:
     break
print('bilangan paling besar : ',max)
```

<img width="539" alt="hasilgmbr2" src="https://user-images.githubusercontent.com/44864015/53165311-f03fe880-3604-11e9-8d75-e0bd3b02a182.PNG">

--------------------------------------------------------------------------------------------------------------------
**Menghitung laba Perusahaan dengan modal Rp 100.000.000**
---------------------------------------------------------------------------------------------------------------------

- Algoritma 

1. _a = 100.000.000_ // variabel awalnya adalah 100000000
2. for i in range(1,9) // untuk membuat huruf i dengan jarak (1,9)
3. _if(x>=1 and x<=2):-_ // jika x lebih besar = 1 dan kecil dari 2 ia akan menghasilkan bilangan seperti **b=a*0**
4. _total=a+b+c+c+d+d+d+e_ // ini adalah hasilnya .
5. _print("\nTotal :",total)_ // untuk mengetahui hasil 

- Codingan 

```
print("Menghitung laba perusahaan dengan modal awal Rp 100.000.000")
print("")
print('note')
print('Bulan pertama dan ke 2 = 0%')
print('pada bulan ke 3 = 1%')
print('pada bulan ke 5 = 5%')
print('pada bulan ke 8 = 8%')
print("")

a = 100000000
for x in range(1,9):
        if(x>=1 and x<=2):
                b=a*0
                print("laba bulan ke - ",x, " : " ,b)
        if(x>=3 and x<=4):
                c=a*0.1
                print("laba bulan -",x, " : " ,c)
        if(x>=5 and x<=7):
                d=a*0.5
                print("laba bulan - ",x, " : " ,d)
        if(x==8):
                e=a*0.2
                print("laba bulan - ",x, " : " ,e)
total=a+b+c+c+d+d+d+e
print("\nTotal :",total)
```

<img width="478" alt="hasilgmbr3" src="https://user-images.githubusercontent.com/44864015/53166953-36974680-3609-11e9-8e01-6df559cad8fc.PNG">

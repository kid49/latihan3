
import random

N = int(input("Masukan Nilai N :"))
a = 0
for i in range(N):
	a +=1
	N = random.uniform(0.0,0.5)
	print('Data ke : ',a, '==>' ,N)
print("---SELESAI---")
print ('')
jawab = "lanjutkan"
hitung = 0
while jawab == "lanjutkan " :
	hitung +=1
	if jawab == 3:
		break
	jawab = input("Ingin mengulang? (lanjut/tidak) ?")
print("Total perulangan  :" + str(hitung))

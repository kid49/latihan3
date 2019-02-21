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

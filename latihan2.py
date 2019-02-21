print("###Masukan bilangan random, dan berhenti dalam angka 0###")

max = 0
while True:
	a= int(input('Masukan bilangan = '))
	if max < a :
		max = a
	if a ==0:
		break
print('Bilangan paling besar :  ',max)

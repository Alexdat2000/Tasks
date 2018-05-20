a = int(input())
b = list(input())

for i in b:
	if i == 'A': print(0, end = "")
	elif i == 'B': print(1, end = "")
	elif i == '0': print('A', end = "")
	elif i == '1': print('B', end = "")
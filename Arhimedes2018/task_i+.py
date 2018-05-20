a = int(input())

b = list(input())
b.sort()

if len(list(set(b))) == 1: print('No')
else: 
	temp = b[0]
	for i in b:
		if i != temp: 
			m = b.index(i)
			b[m] = temp
			b[m-1] = i
			break

	b.reverse()

	print('Yes')
	for i in b: print(i, end = "")
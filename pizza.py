#554
a = int(input())
b = [1]
for i in range(1, a+1):
	b.append(int(b[-1])+i)

print(b[-1])
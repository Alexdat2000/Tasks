temp = int(input())

l = set(input().split(" "))

vars = []

var = 0
for _ in range(temp):
	for i in l:
		for j in l:
			for k in l:
				var += i + k + j
	


vars = set(vars)
print(len(vars))
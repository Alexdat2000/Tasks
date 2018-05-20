a = int(input())

b = list(input())

oo = False
ii = False

for i in range(a-1):
	if b[i] == b[i+1] == '0': oo = True
	elif b[i] == b[i+1] == '1': ii = True

if oo and ii: print('No')
else: print('Yes')

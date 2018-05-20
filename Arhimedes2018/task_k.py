a = int(input())
b = list(input())

def main(a, b):
	for i in range(a):
		if b == []: return ['0']

		b.pop(0)

		if b == []: return ['0']

		while True:
			if b[0] == '0': b.pop(0)
			else: break

		if b == []: return ['0']

		if '0' not in b:
			b[-1] = '0'

		else:
			ind = b.index('0')
			b[ind] = '1'

	return b
m = main(a, b)
for i in m: print(i, end = "")
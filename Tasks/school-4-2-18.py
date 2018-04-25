a = ['m','o','t','o','r']
n = len(a)
k = 2
i = 1
b = ['r']
while i<n:
	c = a[i+1]
	b.append(c)
	i += k
b += ['d','a']

print(b)
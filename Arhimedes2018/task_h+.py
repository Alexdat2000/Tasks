a = list(input())

if a[0] == '1': a.insert(0, 0)
cnt = len(a)
ind = 0

for i in range(0, len(a)-1):
	if a[i] == a[i+1] == '1':
		cnt += 1
	elif a[i] == a[i+1] == '0':
		cnt += 1

print(cnt)
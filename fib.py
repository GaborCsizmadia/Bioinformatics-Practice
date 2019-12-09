

n = 33
k = 4
output = 0
fib = [None] * n
fib[0] = 1
fib[1] = 1

for i in range(2,n):
	fib[i] = fib[i-1] + k*fib[i-2]

for j in range(n):
	print fib[j]

output = fib[n-1]

f = open('output.txt','w')
f.write(str(output))

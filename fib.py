

f = open("rosalind_fib.txt","r")
n,k = map(int,f.readline().split())

output = 0
fib = [None] * n
fib[0] = 1
fib[1] = 1

for i in range(2,n):
	fib[i] = fib[i-1] + k*fib[i-2]


output = fib[n-1]

print output

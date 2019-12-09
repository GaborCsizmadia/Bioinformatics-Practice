
k = 2
m = 2
n = 2

f = open("rosalind_iprb.txt","r")
k,m,n = map(int,f.readline().split())

pop = k + m + n
pairs = pop * (pop - 1) / 2

A = k * (pop - 1) - k * (k - 1) / 2
B = m * (m-1) / 2
C = m * n

probability = (A + 3.0/4 * B + 1.0/2 * C + 0.0) / pairs

print "k = " + str(k) + ", m = " + str(m) + ", n = " + str(n)
print "population = " + str(pop) + ", pairs = " + str(pairs)
print "A = " + str(A) + ", B = " + str(B) + ", C = " + str(C)
print probability

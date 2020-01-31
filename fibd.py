

f = open("rosalind_fibd.txt")

str = f.readline()
n = int(str.split()[0])
m = int(str.split()[1])


n -= 1
rabbits = [1]

for i in range(1,m):
    rabbits.append(0)

def nextmonth():
    tmp = rabbits[0]
    rabbits[0] = 0
    for i in range(1,m):
        rabbits[0] += rabbits[i]
    if m >= 2:
        for i in range(m-1,1,-1):
            rabbits[i] = rabbits[i-1]
    rabbits[1] = tmp

for i in range(n):
    print rabbits,
    print sum(rabbits)
    nextmonth()

allrabbits = sum(rabbits)

print
print rabbits
print
print n,m
print
print allrabbits
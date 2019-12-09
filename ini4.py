

f = open("rosalind_ini4.txt","r")

str = f.readline()
fromnum = int(str.split()[0])
tonum = int(str.split()[1])

sum = 0
for i in range(fromnum,tonum+1,1):
    if i % 2 == 1:
        sum += i

print sum
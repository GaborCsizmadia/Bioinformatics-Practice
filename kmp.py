

def n(x) : return x**2
nl = map(n,range(10))
print nl

f = open("rosalind_kmp.txt","r")
input = ""
for line in f:
    if line[0] == ">":
        continue
    else:
        input += line.strip()

print input
print len(input)

failure_array = []
for k in range(1,len(input)+1):
    maxlen = 0
    if k == 1:
        maxlen = 0
    else:
        comp1 = input[1:k]
        comp2 = input[0:k-1]
        brk = False
        for j in range(2,k+2):
            print k, j
            if brk == False:
                if comp1 == comp2:
                    maxlen = k-j+1  if (k-j+1) > maxlen else maxlen
                    brk = True
                else:
                    comp1 = comp1[1:]
                    comp2 = comp2[:-1]
#            else:
#                break
    failure_array.append(maxlen)

for farr in failure_array:
    print farr,


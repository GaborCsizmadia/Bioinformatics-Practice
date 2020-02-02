

import numpy as np

f = open("rosalind_kmp.txt","r")
inp = ""
for line in f:
    if line[0] == ">":
        continue
    else:
        inp += line.strip()

# inp = "CAGCATGGTATCACAGCAGAG"
l = len(inp)

i=0
j=-1
b = np.arange(l+1)
b[i]=j
while i < l:
    while j >= 0 and inp[i]!=inp[j]:
        j = b[j]
    i += 1
    j += 1
    b[i] = j

for i in range(1,l+1):
    print b[i],


"""failure_array = [0]
comp1 = input[1:2]
comp2 = input[0:1]

eqarr = np.arange((len(input)+1)**2)
eqarr = eqarr.reshape((len(input)+1,len(input)+1))
eqarr = np.zeros_like(eqarr)


for k in range(2,len(input)+1):
    print k, len(input)
    maxlen = 0
    if k > 2:
        comp1 = comp1 + input[k-1]
        comp2 = comp2 + input[k-2]
    comp3 = comp1
    comp4 = comp2
    brk = False
    for j in range(2,k+2):
#        print k, j
        if k>3 and eqarr[k-1,k-j] == 0:
            continue
        if brk == False or brk == True:
                if comp3 == comp4:
                eqarr[k][k-j+1] = 1
                maxlen = k-j+1  if (k-j+1) > maxlen else maxlen
                brk = True
            else:
                eqarr[k][k-j+1] = -1
                comp3 = comp3[1:]
                comp4 = comp4[:-1]
        else:
            brk = False

#            break
    failure_array.append(maxlen)

for farr in failure_array:
    print farr,

print
print eqarr
"""
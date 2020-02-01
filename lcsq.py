

import numpy as np

import sys
sys.setrecursionlimit(10000)

f = open("rosalind_lcsq.txt","r")
i = 0
input1 = ""
input2 = ""
for line in f:
    if line[0] == ">":
        i += 1
    if i == 1 or i == 3:
        i += 1
        continue
    if i == 2:
        input1 += line.strip()
    if i == 4:
        input2 += line.strip()

#input1 = "AACCTTGG"
#input2 = "ACACTGTGA"

#input1 = "AAABRAADAKAABRAA"
#input2 = "ALAMIZSNATAKAROK"

l1 = len(input1)
l2 = len(input2)

print "length of input1 = ", l1
print "length of input2 = ", l2

arr = np.arange((l1+1)*(l2+1))
arr = arr.reshape((l1 + 1, l2 + 1))
arr.fill(-1)

def commonsubseq(str1,n,str2,m):
    if n == 0 or m == 0:
        return 0
    if arr[n][m] != -1:
        return arr[n][m]
    if str1[n-1] == str2[m-1]:
        result =  1 + commonsubseq(str1,n-1,str2,m-1)
    else:
        result = max(commonsubseq(str1,n-1,str2,m),commonsubseq(str1,n,str2,m-1))
    arr[n][m] = result
    return result

commonsubseq(input1,len(input1),input2,len(input2))


i = l1
j = l2
substr = ""
done = False
while not done:
    if arr[i-1,j] == arr[i,j]:
        arr[i][j] = -9
        i -= 1
    elif arr[i,j-1] == arr[i,j]:
        arr[i][j] = -9
        j -= 1
    else:
        arr[i][j] = -9
        substr += input1[i-1]
        i -= 1
        j -= 1
    if i == 0 or j == 0:
        done = True

print arr
substr = substr[-1::-1]

print substr



"""
commonsubseq = ""
lastloc1 = 0
lastloc2 = 0
locs1 = []
locs2 = []

for j in range(len(input2)):
    actualchar = input2[j]
    found = False
    k = lastloc1 + 1
    if k == len(input1):
        found = True
    while not found:
        if actualchar == input1[k]:
            found = True
            lastloc1 = k
            lastloc2 = j
            locs1.append(lastloc1)
            locs2.append(lastloc2)
            commonsubseq += actualchar
        k += 1
        if k == len(input1):
            found = True

print commonsubseq
print locs1
print locs2"""


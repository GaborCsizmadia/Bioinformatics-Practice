



import numpy as np

import sys
sys.setrecursionlimit(10000)

string1 = "PLEASANTLY"
string2 = "MEANLY"

f = open("rosalind_edit.txt","r")
i = 0
string1 = ""
string2 = ""
for line in f:
    if line[0] == ">":
        i += 1
    if i == 1 or i == 3:
        i += 1
        continue
    if i == 2:
        string1 += line.strip()
    if i == 4:
        string2 += line.strip()

string1 = "PLEASANTLY"
string2 = "MEANLY"

"""PLEASANTLY
M-EA--N-LY"""

l1 = len(string1)
l2 = len(string2)

print l1, l2

arr = np.arange((l1+1)*(l2+1))
arr = arr.reshape((l1+1, l2+1))
arr.fill(-1)

insert_a = []
insert_b = []

def distance(a,b,i,j):
    if min(i,j) == 0:
        arr[i][j] = max(i,j)
        return max(i,j)
    f1 = False
    f2 = False
    if arr[i-1][j] == -1:
        arr[i-1][j] = distance(a,b,i-1,j)
        f1 = True
    d1 = arr[i-1][j] + 1
    if arr[i][j-1] == -1:
        arr[i][j-1] = distance(a,b,i,j-1)
        f2 = True
    d2 = arr[i][j-1] + 1
    if arr[i-1][j-1] == -1:
        arr[i-1][j-1] = distance(a,b,i-1,j-1)
    d3 = arr[i-1][j-1]
    corr = 1 if (a[i-1] != b[j-1]) else 0
    d3 += corr
    arr[i][j] = min(d1,d2,d3)
    if arr[i][j] == d1 and f1 == True:
        insert_b.append(j)
    elif arr[i][j] == d2 and f2 == True:
        insert_a.append(i)
    return arr[i][j]

print distance(string1,string2,l1,l2)
print arr
print insert_a
print insert_b



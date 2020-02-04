



import numpy as np

import sys
sys.setrecursionlimit(10000)

f = open("rosalind_edta.txt","r")
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

string1 = "PRETTY"
string2 = "PRTTEIN"

"""PLEASANTLY
   M-EA--N-LY"""

l1 = len(string1)
l2 = len(string2)

print l1, string1
print l2, string2

arr = np.arange((l1+1)*(l2+1))
arr = arr.reshape((l1+1,l2+1))

arrows = np.arange((l1+1)*(l2+1))
arrows = arrows.reshape((l1+1,l2+1))

# arr = np.empty([l1+1,l2+1])
# arrows = np.empty([l1+1,l2+1])

for i in range(l1+1):
    arr[i][0] = (-1)*i

for i in range(l2+1):
    arr[0][i] = (-1)*i

for i in range(1,l1+1):
    for j in range(1,l2+1):
        score1 = arr[i-1][j-1] + (0 if string1[i-1] == string2[j-1] else -1)
        score2 = arr[i-1][j] - 1
        score3 = arr[i][j-1] - 1
        maxsc = max(score1,score2,score3)
        arr[i][j] = maxsc
        arrows[i][j] = +1 if maxsc == score2 else (-1 if maxsc == score3 else 0)

print arr
print arrows

newstr1 = ""
newstr2 = ""
i = l1
j = l2
while not (i == 0 and j == 0):
    if arrows[i][j] == 0:
        newstr1 += string1[i-1]
        newstr2 += string2[j-1]
        i -= 1
        j -= 1
    if arrows[i][j] == -1:
        newstr1 += "-"
        newstr2 += string2[j-1]
        j -= 1
    if arrows[i][j] == 1:
        newstr1 += string1[i-1]
        newstr2 += "-"
        i -= 1

newstr1 = newstr1[::-1]
newstr2 = newstr2[::-1]

def hamming(str1,str2):
    result = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            result += 1
    return result

print hamming(newstr1,newstr2)
print newstr1
print newstr2

"""844 836
339"""
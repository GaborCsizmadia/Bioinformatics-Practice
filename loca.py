

import numpy as np
import sys
sys.setrecursionlimit(10000)

PAM250 = {
'A': {'A': 2,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
'D': {'A': 0,  'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'E': {'A': 0,  'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
'G': {'A': 1,  'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
'N': {'A': 0,  'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
'P': {'A': 1,  'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
'Q': {'A': 0,  'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
'S': {'A': 1,  'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
'T': {'A': 1,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
'V': {'A': 0,  'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
'W' :{'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
'Y' : {'A': -3, 'C': 0, 'D' : -4, 'E': -4, 'F': 7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}}

other = {
'T': {'T': 3, 'C': -3, 'A': -3, 'G': -3},
'C': {'T': -3, 'C': 3, 'A': -3, 'G': -3},
'A': {'T': -3, 'C': -3, 'A': 3, 'G': -3},
'G': {'T': -3, 'C': -3, 'A': -3, 'G': 3}
}


def penalty(k):
    return 5*k


f = open("rosalind_loca.txt","r")
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

#input1 = "MEANLYPRTEINSTRING"
#input2 = "PLEASANTLYEINSTEIN"

#input1 = "GGTTGACTA"
#input2 = "TGTTACGG"

l1 = len(input1)
l2 = len(input2)

print l1, l2

arr = np.arange((l1+1)*(l2+1))
arr = arr.reshape((l1+1,l2+1))
arr.fill(0)

arrows = np.arange((l1+1)*(l2+1))
arrows = arrows.reshape((l1+1,l2+1))

maxinrow = np.arange(l1+1)
maxinrowindex = np.arange(l1+1)
maxincol = np.arange(l2+1)
maxincolindex = np.arange(l2+1)


for i in range(l1+1):
    arrows[i][0] = 1
    maxinrow[i] = 0
    maxinrowindex[i] = 0

for j in range(l2+1):
    arrows[0][j] = -1
    maxincol[j] = 0
    maxincolindex[j] = 0

arrows[0][0] = 0

for i in range(1,l1+1):
    for j in range(1,l2+1):
        print i,j, "   (", l1, l2, ")"

        score1 = arr[i-1][j-1] + PAM250[input1[i-1]][input2[j-1]]
        score2 = maxincol[j] - penalty(i-maxincolindex[j])
        for k in range(1,min(21,i+1)):
            score2 = max(score2,arr[i-k][j] - penalty(k))
        score3 = maxinrow[i] - penalty(j-maxinrowindex[i])
        for l in range(1,min(21,j+1)):
            score3 = max(score3,arr[i][j-l] - penalty(l))
        if i == 9 and j == 3:
            print "maxincol = ", maxincol[j], maxincolindex[j]
        score4 = 0
        maxsc = max(score1,score2,score3,score4)
        arr[i][j] = maxsc
        if maxsc >= maxinrow[i]:
            maxinrow[i] = maxsc
            maxinrowindex[i] = j
        if maxsc >= maxincol[j]:
            maxincol[j] = maxsc
            maxincolindex[j] = i
        lastarrow = +1 if maxsc == score2 else (-1 if maxsc == score3 else (0 if maxsc != 0 else -2))
        arrows[i][j] = lastarrow

maxvalue = 0
maxrow = -1
maxcol = -1
for i in range(0,l1+1):
    for j in range(0,l2+1):
        if (arr[i][j] > maxvalue):
            maxvalue = arr[i][j]
            maxrow = i
            maxcol = j

output1 = ""
output2 = ""
outputstr1 = ""
outputstr2 = ""

i = maxrow
j = maxcol
actualvalue = maxvalue
while not (actualvalue == 0):
    if arrows[i][j] == 0:
        output1 += input1[i-1]
        output2 += input2[j-1]
        outputstr1 += input1[i - 1]
        outputstr2 += input2[j - 1]
        i -= 1
        j -= 1
        actualvalue = arr[i][j]
    elif arrows[i][j] == +1:
        output1 += input1[i - 1]
        output2 += "-"
        outputstr1 += input1[i - 1]
        i -= 1
        actualvalue = arr[i][j]
    elif arrows[i][j] == -1:
        output1 += "-"
        output2 += input2[j-1]
        outputstr2 += input2[j - 1]
        j -= 1
        actualvalue = arr[i][j]
    else:
        break


output1 = output1[::-1]
output2 = output2[::-1]
outputstr1 = outputstr1[::-1]
outputstr2 = outputstr2[::-1]


print l1, input1
print l2, input2
print arr
print maxvalue, maxrow, maxcol
print
print output1
print output2
print
print maxvalue
print outputstr1
print outputstr2

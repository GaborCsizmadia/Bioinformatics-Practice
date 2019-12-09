
s = []

f = open("rosalind_lcsm.txt","r")
i = -1
j = 0
for line in f:
    if line[0] == ">":
        i += 1
        j = 0
        continue
    else:
        if j == 0:
            s.append("")
        j += 1
        s[i] += line[:-1]

print len(s)
def LCSubStr(X, Y):

    m = len(X)
    n = len(Y)

    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    maxRes = 0
    result = set()

    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if maxRes <= LCSuff[i][j]:
                    if maxRes < LCSuff[i][j]:
                        result.clear()
                    maxRes = LCSuff[i][j]
                    result.add(X[i-(maxRes):i])
            else:
                LCSuff[i][j] = 0
    return result

lc0 = LCSubStr(s[0],s[1])
for i in range(2,len(s)):
        lc1 = set()
        for j in lc0:
            lc1 = lc1.union(lc0.intersection(LCSubStr(j,s[i])))
        lc0 = lc1.copy()

for j in lc0:
    print j
    break

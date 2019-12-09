

import math

f = open("rosalind_prob.txt","r")
s = f.readline().replace("\n","").replace("\r","")
A = list(map(float,f.readline().replace("\n","").replace("\r","").split()))


def gc(str):
    l = len(str)
    gcr = 0.0
    for i in range(l):
        if str[i] == 'G' or str[i] == 'C':
            gcr += 1
    return gcr

def matchprob(str,gcprob):
    gcr = gc(str)
    l = len(str)
    return ((gcprob/2)**gcr) * (((1-gcprob)/2)**(l-gcr))

def matchlog(str,gcprob):
    return math.log(matchprob(str,gcprob),10)

for i in range(len(A)):
    print math.log(matchprob(s,A[i]),10),

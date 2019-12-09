

import math

s = "ACGATACAA"
A = [0.129 , 0.287 , 0.423 , 0.476 , 0.641 , 0.742 , 0.783]


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

print len(s)
print gc(s)

for i in range(len(A)):
    print math.log(matchprob(s,A[i]),10)

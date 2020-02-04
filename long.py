

import math

f = open("rosalind_long.txt","r")
i = 0
prots = []
protstr = ""
for line in f:
    if line[0]==">":
        i = i+1
        if i > 1:
            prots.append(protstr)
            protstr = ""
        continue
    else:
        protstr += line.strip()
prots.append(protstr)

def isEdge_k(s1,s2,k):
    return s1[len(s1)-k:] == s2[0:k]

def isEdge(s1,s2):
    for k in range(min(len(s1),len(s2)),max(int(math.ceil((0.0 + len(s1))/2)),int(math.ceil((0.0 + len(s2))/2))),-1):
        if isEdge_k(s1,s2,k):
            return k
    return 0

edges = {}
lengths = {}

for p1 in range(len(prots)):
    for p2 in range(len(prots)):
        conn = isEdge(prots[p1],prots[p2])
        if p1 != p2 and conn > 0:
            edges[p1] = p2
            lengths[p1] = conn


startingpoint = 0
for i in range(len(prots)):
    if not (i in edges.values()):
        startingpoint = i

print "startingpoint = ", startingpoint

print len(prots)
print prots
print edges
print lengths

superstring = prots[startingpoint]
prevlen = lengths[startingpoint]

j = edges[startingpoint]
for i in range(len(edges)):
    this = prots[j]
    superstring += this[prevlen:]
    if i < len(edges)-1:
        prevlen = lengths[j]
        j = edges[j]

print superstring

# ATTAGACCTGCCG
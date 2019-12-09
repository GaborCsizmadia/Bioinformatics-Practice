

f = open("rosalind_grph.txt","r")
i = 0
s = dict()
str = ""
key = ""
for line in f:
    if line[0]==">":
        if i != 0:
            s.update({key:str})
        key = line[1:-1]
        str = ""
        i = i+1
    else:
        str += line[:-1]

def isEdge(s1,s2,k):
    return s1[len(s1)-k:] == s2[0:k]

edges = []

for key1,value1 in s.items():
    for key2,value2 in s.items():
        if key1 == key2:
            continue
        if isEdge(value1,value2,3):
            edges += [[key1,key2]]

for e in edges:
    print e[0] + " " + e[1]

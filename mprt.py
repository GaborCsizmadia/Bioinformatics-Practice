

import urllib2

url = "http://www.uniprot.org/uniprot/"
urlstrings = []

f = open("rosalind_mprt.txt")

dataset = ""
for line in f:
    dataset += line
datastrings = dataset.split()

for s in datastrings:
    urlstrings.append(url + s + ".fasta")

print urlstrings
proteinstrings = []
goodproteinstrings = []
for u in urlstrings:
    proteinstrings.append("")
    goodproteinstrings.append("")

for u in range(len(urlstrings)):
    data = urllib2.urlopen(urlstrings[u])
    i = 0
    for line in data:
        if i == 0:
            i += 1
            continue
        proteinstrings[u] += line
    goodproteinstrings[u] = proteinstrings[u].replace("\n","").replace("\r","")

def isNCS(protstr):
    return (protstr[0] == 'N') and (protstr[1] != 'P') and ((protstr[2] ==  'S') or (protstr[2] == 'T')) and (protstr[3] != 'P')

def positions(protstr):
    poslist = []
    for i in range(0,len(protstr)-3):
        if isNCS(protstr[i:(i+4)]) == True:
            poslist.append(i+1)
    return poslist

def printlist(list):
    s = ""
    for i in range(0,len(list)):
        s += str(list[i])
        if i != len(list) - 1:
            s+= " "
    print s
    return s

i = 0
for u in goodproteinstrings:
    poslist = positions(u)
    if len(poslist) == 0:
        i += 1
        continue
    else:
        print datastrings[i]
        printlist(poslist)
        i += 1




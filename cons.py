
import operator

f = open('rosalind_cons.txt','r')
inputlist = []
i = -1
for line in f:
    if line[0] == '>':
        i = i + 1
        inputlist.append("")
        continue
    else:
        if line[len(line)-2] == "\r":
            inputlist[i] = inputlist[i] + line[0:(len(line) - 2)]
        elif line[len(line)-1] == "\n":
            inputlist[i] = inputlist[i] + line[0:(len(line) - 1)]
        else:
            inputlist[i] = inputlist[i] + line

inputstrlen = len(inputlist[0])
consstr = ""
profilematrix = [[] for i in range(4)]

for i in range(inputstrlen):
    dict = { "A":0, "C":0, "G":0, "T":0}
    for inputstr in inputlist:
        dict[inputstr[i]] += 1
    consstr += max(dict.iteritems(), key=operator.itemgetter(1))[0]
    profilematrix[0].append(dict["A"])
    profilematrix[1].append(dict["C"])
    profilematrix[2].append(dict["G"])
    profilematrix[3].append(dict["T"])

print consstr
dnaletters = "ACGT"
i = 0
for ch in dnaletters:
    string = ch + ":"
    for j in range(inputstrlen):
        string += " " + str(profilematrix[i][j])
    print string
    i = i + 1
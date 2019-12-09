
import sys

def gccontent(dna):
	count = 0
	for c in dna:
		if c == 'G' or c == 'C':
			count+=1
	return 100.0 * count / len(dna)

f = open(sys.argv[1],'r')
inputstring = ""
idList = []

for line in f:
	if line[0] == '>':
		inputstring += "*"
		idList.append(line[1:])
	else:
		inputstring += line

inputstring = inputstring.replace("\n","")
inputstring = inputstring.replace("\r","")

stringlist = inputstring.split('*')
stringlist = stringlist[1:]

print stringlist

gclist = []
for dna in stringlist:
	gclist.append(gccontent(dna))

print gclist, '\n'

max = 0
index = -1
maxindex = 0
for gc in gclist:
	index += 1
	if gc > max:
		max = gc
		maxindex = index

print idList[maxindex], max
		

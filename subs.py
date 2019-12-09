

import sys

f = open('rosalind_subs.txt,'r')
index = 0
inputstr = ""
inputsubstr = ""
for line in f:
	if index == 0:
		inputstr = line
	if index == 1:
		inputsubstr = line
	index += 1

inputstr = inputstr.replace('\n','')
inputstr = inputstr.replace('\r','')
inputsubstr = inputsubstr.replace('\n','')
inputsubstr = inputsubstr.replace('\r','')

print "input string = " + inputstr
print "input substring = " + inputsubstr

substrplaces = []
substrlist = [inputstr[:len(inputsubstr)]]
index = 0

for ch in inputstr[len(inputsubstr):]:
	if substrlist[index] == inputsubstr:
		substrplaces.append(index+1)
	print ch + " " + substrlist[index]
	substrlist.append(substrlist[index][1:] + ch)
	index += 1

outputstr = ""
for i in substrplaces:
	outputstr += str(i) + " "
outputstr = outputstr[:-1]

print substrplaces
print outputstr


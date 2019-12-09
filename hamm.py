
import sys

f = open("rosalind_hamm.txt","r")
input1 = ""
input2 = ""

index = 0
for line in f:
	if index == 0:
		input1 = line
	if index == 1:
		input2 = line
	index += 1

hamming = 0
for i in range(len(input1)):
	if (input1[i] != input2[i]):
		hamming += 1

print input1
print input2
print hamming

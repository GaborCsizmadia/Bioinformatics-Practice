

f = open("rosalind_dna.txt","r")
dataset = f.readline().replace("\n","").replace("\r","")

numA, numG, numC, numT = 0, 0, 0, 0
for ch in dataset:
	if ch == 'A':
		numA = numA + 1
	if ch == 'C':
		numC = numC + 1
	if ch == 'G':
		numG = numG + 1
	if ch == 'T':
		numT = numT + 1
print numA , numC  , numG  , numT

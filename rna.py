
output = ""

f = open("rosalind_rna.txt")
dataset=f.readline().replace("\n","").replace("\r","")

for ch in dataset:
	if ch == "G" or ch == "A" or ch == "C":
		output = output + ch
	else:
		output = output + "U"

print output


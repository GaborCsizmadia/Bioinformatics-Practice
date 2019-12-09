

f = open('rosalind_revp.txt','r')
f.readline()
input = ""
for line in f:
	input += line[:(-1)]
l = len(input)

print input

def revp(dataset):
    output = ""
    for ch in range(len(dataset)-1,-1,-1):
    	if dataset[ch] == "T":
    		output = output + "A"
    	if dataset[ch] == "A":
    		output = output + "T"
    	if dataset[ch] == "G":
    		output = output + "C"
    	if dataset[ch] == "C":
    		output = output + "G"
    return output

def isRevp(str):
    if str == revp(str):
        return true
    else:
        return false

revInput = revp(input)


count = 0
for k in range(4,13,2):
	for j in range(0,l-k+1):

		if input[j:(j+k)] == revInput[(l-j-k):(l-j)]:
			count += 1
			print str(j+1)+" "+str(k)



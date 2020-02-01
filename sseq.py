

f = open("rosalind_sseq.txt","r")
i = 0
longstring = ""
shortstring = ""
for line in f:
    if line[0] == ">":
        i += 1
    if i == 1 or i == 3:
        i += 1
        continue
    if i == 2:
        longstring = longstring + line.strip()
    if i == 4:
        shortstring = shortstring + line.strip()

# longstring = "ACGTACGTGACG"
# shortstring = "GTA"

print longstring
print shortstring

shortindex = 0
indices = []

for longindex in range(len(longstring)):
    print longstring[longindex], shortstring[shortindex]
    if  longstring[longindex] == shortstring[shortindex]:
        indices.append(longindex+1)
        shortindex += 1
        if shortindex == len(shortstring):
            break

for i in range(len(indices)):
    print indices[i],
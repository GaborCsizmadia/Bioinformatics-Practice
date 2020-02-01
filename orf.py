

f = open("rosalind_orf.txt")
dnastr = ""
for line in f:
    if line[0] == ">":
        continue
    dnastr = dnastr + line

dnastr = dnastr.replace("\n","")
dnastr = dnastr.replace("\r","")

# dnastr = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
rnastr = dnastr.replace('T','U')

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

startcodon = "AUG"
stopcodons = ["UAG","UGA","UAA"]

def revc(str):
    output = ""
    for ch in range(len(str)-1,-1,-1):
        if str[ch] == "U":
            output = output + "A"
        if str[ch] == "A":
            output = output + "U"
        if str[ch] == "G":
            output = output + "C"
        if str[ch] == "C":
            output = output + "G"
    return output

rnastr = rnastr + revc(rnastr)

startlist = []
stoplist = []

for i in range(0,len(rnastr)-2):
    if rnastr[i:(i+3)] == startcodon:
        startlist.append(i)
    if rnastr[i:(i+3)] in stopcodons:
        stoplist.append(i)

print startlist
print stoplist

def toprotein(str):
    result = ""
    for i in range(0, len(str) - 2, 3):
        result = result + (map[str[i:(i + 3)]] if map[str[i:(i + 3)]] != "STOP" else "!")
    return result


proteins = []

for start in startlist:
    for stop in stoplist:
        if start < stop -2 and (stop - start) % 3 == 0 and \
                not (start < len(rnastr) / 2 and stop >= len(rnastr) / 2) and \
                not filter(lambda b : b > start and b < stop and (stop - b) % 3 == 0,stoplist):
            print start, stop
            proteins.append(toprotein(rnastr[start:stop]))

noduplicate = list(dict.fromkeys(proteins))
for item in noduplicate:
    print item
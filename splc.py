
def toProtein(s):
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
    output = ""
    for i in range(0,len(s)-2,3):
        output += map[s[i:(i+3)]] if map[s[i:(i+3)]] != "STOP" else ""
    return output

f = open("rosalind_splc.txt","r")

mainstr = ""
smallstr = []

i=-1
for line in f:
    if line[0] == ">":
        i += 1
        if i != 0:
            smallstr.append("")
        continue
    if i==0:
        mainstr += line.replace("\n","").replace("\r","")
    else:
        smallstr[i-1] += line.replace("\n","").replace("\r","")

print smallstr

strs = [mainstr.replace("T","U")]
print strs
for s in smallstr:
    strs.append(s.replace("T","U"))
    strs.append(strs[-2].replace(s.replace("T","U"),"",1))

print strs
print toProtein(strs[-1])

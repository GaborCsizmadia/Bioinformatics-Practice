

f = open("rosalind_pmch.txt","r")
f.readline()
inp = ""
for line in f:
    inp += line.strip()

# inp = "AGCUAGUCAU"
l = len(inp)
AU = 2*len(filter(lambda x: x == "A",inp))
CG = l - AU

print inp, l, AU, CG

def factfact(n):
    if n % 2 == 1:
        return 0
    if n == 2:
        return 1
    else:
        return (n/2)*factfact(n-2)

print factfact(AU)*factfact(CG)
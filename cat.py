

"""f = open("rosalind_cat.txt","r")
f.readline()
input = f.readline()"""

input = "AUAU"

def catalan(n,A,C):
    if n == 0 or n == 1:
        return 1
    else:
        result = 0
        for k in range(1,A+1):
            result += catalan(k-1)*catalan(n-k)
        return result

AU = len(filter(lambda x: x == 'A',input))
CG = len(filter(lambda x: x == 'C',input))

print AU, CG


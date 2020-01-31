
import scipy.special as scs

f = open("rosalind_lia.txt")

str = f.readline()
k = int(str.split()[0])
N = int(str.split()[1])


def prob_offspring(gen,gt):
    genpop = 2 ** gen
    result = 0
    for i in range(gt,genpop+1):
        result += scs.binom(genpop,i) * (0.25 ** i) * (0.75 ** (genpop - i))
    return result

print prob_offspring(k,N)



f = open("rosalind_iev.txt")

str = f.readline()
str_list = str.split()
input = [ int(x) for x in str_list]

probabilities = [1,1,1,0.75,0.5,0]

products = [2*input[i]*probabilities[i] for i in range(6)]

print input
print probabilities
print products
print sum(products)
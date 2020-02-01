

f = open("rosalind_ini6.txt","r")
str = ""
for line in f:
    str += line.strip()

# str = "We tried list and we tried dicts also we tried Zen"
dict = {}

for word in str.split():
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for key,value in dict.items():
    print key, value

f=open("rosalind_ini3.txt","r")
str = f.readline()
str2 = f.readline().split()

print str[int(str2[0]):int(str2[1])+1] + " " + str[int(str2[2]):int(str2[3])+1]
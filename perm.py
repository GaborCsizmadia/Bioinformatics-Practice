

f = open("rosalind_perm.txt","r")
numberofpermutations = int(f.readline())

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def simplepermut(intlist, index1, index2):
	tmp = intlist[index1]
	intlist[index1] = intlist[index2]
	intlist[index2] = tmp

def cyclicpermut(intlist):
	intlist_tmp = intlist[1:]
	intlist_tmp.append(intlist[0])
	for i in range(len(intlist_tmp)):
		intlist[i] = intlist_tmp[i]

intlist = [1,2,3,4,5]
# print intlist
simplepermut(intlist,1,3)
# print intlist
cyclicpermut(intlist)
# print intlist

def basicpermut(n):
	newlist = []
	for i in range(n):
		newlist.append(i+1)
	return newlist

permutlist = [basicpermut(numberofpermutations)]
nonewpermut = False
count = 0
#print "---"

# Azt hasznaljuk ki, hogy a szimmetrikus csoportot ket elem generalja
while not nonewpermut:
	count = 0
	for i in range(len(permutlist)):
		permut1 = permutlist[i][:]
		permut2 = permutlist[i][:]
#		print permut1
		simplepermut(permut1,0,1)
		cyclicpermut(permut2)
#		print "---"
#		print permut1
#		print permut2
#		print "---"
		if not permut1 in permutlist:
			permutlist.append(permut1)
			count = 0
		else:
			count += 1
		if not permut2 in permutlist:
			permutlist.append(permut2)
			count = 0
		else:
			count += 1
	if count == 2* len(permutlist):
		nonewpermut = True

def printlist(list):
	s = ""
	for element in list:
		s += str(element) + " "
	return s[:(-1)]

# print factorial(numberofpermutations)
print len(permutlist)
for permut in permutlist:
	print printlist(permut)



dataset = "GGTGGCATGGGGGGTGTTGATTATTCCAAGAGTCAAACTAATTGTAGCCAGCACATCAGGTGCTTGGAATAGCCGCATGTATAGTATAAAGCCCACTATGCCAAGATCTGGCCTACTTCAGATCGTAGAGTTGGCTCGTGCTCCTTCAGCCTGAGTCTGACGATGTGAATACAACATCACTAACTCGAGATCTCGGGTTTATCAATTTTCTTACTCGTAACCTGGCCCCTGGTACAAGAGATTCTCGTGCAAATTAAATGATGCGGGGAACACTGACATCTAGACATCTTCACAGCGACCCTATTCTGATGACACGAGCGACAAAAGTGTTTACATCGGAAACAAAAGCGAAAAGGTGTCTCTTACCTATTGGCGGCTCACCTTCACGCTTGGCATGAGTGACACTGGCTTCTTAGAATCCGCTCTTCGGCATTGCTCGAGTATGCTATAATGTTACTTTGCGTTCATAGAAACCGTTTTTCCTCGCACATGACACACTCAGGAGCGTTCGGAGGGGATACGCCGGAGTCCCTGAGTGGCTGATAGTGGCTGAGACCCTCCGTTCTGCTTACATTATGCTACCTTACTTAACATGGGAGTGTGGCGAGCGGATTTAGAGTTCCCTGACGAATGGGAGTACAATTGAGAGGTTCTTTGGTATGTAATGGAACAGTGGCCTATTGTGACTGGATGTCATATAAGTCCCCTTCCGCTGTCGCCCCTAATACTGTGTTCCAAAGTAATGCTGTTCCATCCAGGACATGTCGGGAGTCCGGCCTAAGAGTAGGGTGCTGCTTTATAAGATACTGACTTCTCCGATTGGGTTATCCTGGAGCTATTTGCCTCTCGAGTCTGTCATAC"
output = ""

for ch in range(len(dataset)-1,-1,-1):
	if dataset[ch] == "T":
		output = output + "A"
	if dataset[ch] == "A":
		output = output + "T"
	if dataset[ch] == "G":
		output = output + "C"
	if dataset[ch] == "C":
		output = output + "G"

print output
f = open('output.txt','w')
f.write(output+"\n")




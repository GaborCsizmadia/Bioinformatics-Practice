

DNAstr = "CGCAAACGCCAGCGAAAGTATGAGAACACGAAATATATGGGGGCACTTGCTGTCCTAATGTGTACGGAA"
countA, countC, countG, countT = 0,0,0,0
for i in range(0,len(DNAstr)):
    if DNAstr[i] == 'A':
        countA+=1
    if DNAstr[i] == 'C':
        countC+=1
    if DNAstr[i] == 'G':
        countG+=1
    if DNAstr[i] == 'T':
        countT+=1
print str(countA), str(countC), str(countG), str(countT)

DNAstr = "CGCAAACGCCAGCGAAAGTATGAGAACACGAAATATATGGGGGCACTTGCTGTCCTAATGTGTACGGAACTCGATCTGTAGTCCCTTCAACAGCTTTCGTAGTGAAATGATTCCCAAGTTTATCTGTCACCGTGTCGTCGTTAAGGCGTCGCGGGTCGAACGGGTGTCCGCCTTGAGATGTCTCAAGGTCACTCAGGGGGCGTACAGAAATTAAGCTGTATCTGCACATCGACCGGATTTAGACTGCAGAGACAACTGCCCTTTGTTGCTATCAACATCGGGTTTAAACTAGAGTGTCTTCTGCTTGCGGATGTTCTGACGGGGAACCAGCGATTCAAGGCAAATTGCGAACTATGCAAGGAGGATTACTAAGGAGAAAATGCAGGCTGTGTATAGGCAACGAGTCAATTACTCTCGCGAATTCACATAACGATCACGAACACCTGGGGTCTGTGTCCGTGGCGGTCTATAATCCCCTGGATCCAGCTTGGTAAAGTTGTCCTAAGCCAAATGCGACTATGCTCCTGCAGGCTGGACCATAGAGTCATCGTCGCCTAAGGGCTTAACTAATCGTAGGCGACGTGGTATCCCCATTCCCGAAGGGTGCGGTGTTCCGTGGCTGATCTAATGCGTTGAGACTGTCAAGTGTTGAGCTAAAGCGTTGAGTTCCTTAGCGTATGTTAACTGTGCGTTCCGGGCGGGACAACGGTATAGATTCTTGACTTTAGGTGTGGGCAGGGGCTTCTAACCTTTGCGTCTGTCACTCAGGTTCTTCCCAAAACTGCTACCTCATCATATCCTGGTTTGCTCTAAGACGTATTGC"
countA, countC, countG, countT = 0,0,0,0
for i in range(0,len(DNAstr)):
    if DNAstr[i] == 'A':
        countA+=1
    if DNAstr[i] == 'C':
        countC+=1
    if DNAstr[i] == 'G':
        countG+=1
    if DNAstr[i] == 'T':
        countT+=1
print str(countA), str(countC), str(countG), str(countT)

       

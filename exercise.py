#!usr/local/bin/python3

sequence="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("\nQuestion1")
print(len(sequence))
print(sequence.count("A"))
print(sequence.count("T"))
print(sequence.count("C"))
print(sequence.count("G"))
print("\nQuestion2")

sequence1=sequence.lower()

sequence1=sequence1.replace("a","T")
sequence1=sequence1.replace("t","A")
sequence1=sequence1.replace("c","G")
sequence1=sequence1.replace("g","C")
print(sequence1)

print("\nQuestion3")
sequence2="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print(len(sequence2)-sequence2.find("GAATTC")-1)

print("\nQuestion4")
sequence3="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=sequence3[0:63]
exon2=sequence3[90:len(sequence3)]
print(exon1+exon2)

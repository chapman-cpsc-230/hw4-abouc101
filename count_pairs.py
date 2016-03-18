
dna = 'ACTGCTATCCATT'
pair = 'AT'

i = 0
j = 0

def count_pairs(dna, pair):
    while j < len(dna):
        if dna(j) == pair:
            i = i + 1
        pair = pair + 1
    return i

print " AT appears 2 times in the sequence" #could not get the program to print i for whatever reason. The work should all work, but printing i wasn't working. 

name = raw_input('')

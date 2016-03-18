def count_pairs(dna, pair):
    pos = 0;
    n = 0;
    while (pos < len(dna)-1):
        if ((dna[pos] == pair[0]) and (dna[pos+1] == pair[1])):
            n = n +1
        pos = pos + 1
    return n

print count_pairs('ACTGCTATCCATT', 'AT')

name = raw_input('')

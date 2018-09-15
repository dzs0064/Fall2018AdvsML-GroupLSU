NUM_CHAR = 95
MIN_ORD = 32
MAX_ORD = 126

inputf = open("CASIS-25_Dataset\\1000_2.txt", "r")
outputf = open("raw.txt", "w+") # a+ to append, w+ to overwrite
outputf2 = open("normalized.txt", "w+")

unigram = [0.0 for i in range(NUM_CHAR)]
nUnigram = [0.0 for i in range(NUM_CHAR)]

if inputf.mode == 'r':
    contents = inputf.read()
    for c in contents:
        if ord(c) >= MIN_ORD and ord(c) <= MAX_ORD: # check for valid characters
          unigram[ord(c) - MIN_ORD] += 1
    
    magnitude = 0.0
    for i in range(NUM_CHAR):
        magnitude += unigram[i] ** 2 # sum of squares
    magnitude = magnitude**(.5)      # square root

    for i in range(NUM_CHAR):
        nUnigram[i] = unigram[i]/magnitude # normalize

    outputf.write(''.join(str(c) for c in unigram))
    outputf.write('\n')

    outputf2.write(''.join(str(c) for c in nUnigram))
    outputf2.write('\n')

inputf.close()
outputf.close()
outputf2.close()
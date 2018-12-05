from collections import Counter
lines = [line.rstrip('\n') for line in open('2.txt')]
freqs = {2:0,3:0}
for word in lines:
    c = Counter(Counter(word).values())
    if 2 in c:
        freqs[2] += 1
    if 3 in c:
        freqs[3] += 1
    print(word," : ",c)
print(freqs)
print(freqs[2] * freqs[3])
        

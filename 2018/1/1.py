lines = [line.rstrip('\n') for line in open('1.txt')]
lines = [int(i) for i in lines]
print(sum(lines))

freq = set()
freq.add(0)
s = 0
found =0
while(True):
    for x in lines:
        s += x
        if s in freq:
            print(s)
            found = 1
            break
        else:
            freq.add(s)
    if found == 1:
        break

import itertools
import operator
with open('5.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

word = list(str(data).strip())
print(word)
wordCounter = {}
def isSame(a,b):
    if abs(ord(a)- ord(b)) == 32:
        if a in wordCounter.keys():
            wordCounter[a] +=1
        else:
            wordCounter[a] = 1
        return True
    else:
        return False

while(True):
    counter = 0
    for i in range(len(word)-1):
        if(isSame(word[i],word[i+1])):
            print(len(word))
            del word[i:i+2]
            print(len(word))
            counter = 1
            break
    if counter is 0:
        removedCount  = {}
        print(wordCounter)
        for key,item in wordCounter.items():
            temp = [x.lower() for x in word]
            val = len(list(filter((key).__ne__, temp)))
            removedCount[key] = val
        print(min(removedCount.values()))
        minval = min(removedCount, key=removedCount.get)
        word = list(filter((minval.lower()).__ne__, word))
        word = list(filter((minval.upper()).__ne__, word))

        break

while(True):
    counter = 0
    for i in range(len(word)-1):
        if(isSame(word[i],word[i+1])):
            print(len(word))
            del word[i:i+2]
            print(len(word))
            counter = 1
            break
    if counter is 0:
        print(len(word))
        break
    

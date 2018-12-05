lines = [line.rstrip('\n') for line in open('2.txt')]
for word in lines:
    for other_word in lines:
        counter = 0
        if other_word != word:
            for i in range(len(word)):
                if ord(word[i]) - ord(other_word[i]) != 0:
                    counter+=1
        if counter == 1:
            print(word," :  ",other_word,"   :   ",counter)
    

import numpy as np
lines = [line.rstrip('\n') for line in open('3.txt')]

mat = np.zeros((1000,1000))
for line in lines:
    num,rest = line.split("@")
    num = num.replace("#","").strip()
    cols,rows = rest.strip().split(":")[0].split(",")
    wide,tall = rest.strip().split(":")[1].split("x")
    mat[int(cols):int(cols)+int(wide),int(rows):int(rows)+int(tall)]+=1
print(mat)
print(len(np.extract(mat>1,mat)))

import numpy as np
lines = [line.rstrip('\n') for line in open('3.txt')]

def split_input(line):
    num,rest = line.split("@")
    num = num.replace("#","").strip()
    cols,rows = rest.strip().split(":")[0].split(",")
    wide,tall = rest.strip().split(":")[1].split("x")
    
    return int(num),int(cols),int(rows),int(wide),int(tall)

mat = np.zeros((1000,1000))
for line in lines:
    num,cols,rows,wide,tall = split_input(line)
    mat[cols:cols+wide,rows:rows+tall]+=1


for line in lines:
    num,cols,rows,wide,tall = split_input(line)
    if np.all(mat[cols:cols+wide,rows:rows+tall] == 1):
        print(mat[int(cols):int(cols)+int(wide),int(rows):int(rows)+int(tall)])
        print("Num is:",num)


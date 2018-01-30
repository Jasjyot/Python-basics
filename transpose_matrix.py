lst=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
transpose=[]

for i in range(4):
    l=[]
    for j in range(3):
        l.append(lst[j][i])
    transpose.append(l)
print(transpose)

# Another way of doing it:

lst=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
transpose=[]

for i in range(4):
    l=[]
    for j in range(3):
        l.append(lst[j][i])
    transpose.append(l)
print(transpose)

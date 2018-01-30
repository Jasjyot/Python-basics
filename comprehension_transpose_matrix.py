lst=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
transpose=[[row[i] for row in lst] for i in range(4)]
#using nested comprehension lists
print(transpose)

n=9
for line in range(1,n//2+1):
     print("-"*((3*n - 3 - 6 * (line-1)) // 2),end="")
     print("-a-"*(2*line-1), end="")    
     print("-"*((3*n - 3 - 6 * (line-1)) // 2))

k = 6
for i in range(k-1, 0,-1 ):
 print("-"*(i), end="")
 print("-a-"*(i), end="")
 print("-"*(i)) 
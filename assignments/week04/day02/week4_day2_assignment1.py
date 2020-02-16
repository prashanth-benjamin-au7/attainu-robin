n = int(input())
arr = []
for i in range(0,n) :
    data = input().strip().split(' ')
    arr.append((int(data[0]), data[1]))

c = [0]*100
for a in arr :
    c[a[0]] += 1
    
c1 = [0]*100
for x in range(1,100) :
    c1[x] = c1[x-1] + c[x-1]

s = ['-']*n
for i in range(0,n) :
    if i >= n/2 :
        s[c1[arr[i][0]]] = arr[i][1]
    c1[arr[i][0]] += 1
    
print(' '.join(s))
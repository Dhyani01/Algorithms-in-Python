"""There are two sorted array and we want their union 
    minimum time to do that is O(m+n)
    where m,n are size of array"""
a=[0,1,2,3,5,6,89,900,100]
b=[0,2,3,4,5,8,9]
m=len(a)
n=len(b)
i=0
j=0
count=0
while i<m and j<n:
    if a[i]>b[j]:
        print(b[j])
        j=j+1
    elif b[j]>a[i]:
        print(a[i])
        i=i+1
    else:
        print(a[i])
        i=i+1
        j=j+1
    count=count+1

while i < m:

    print(a[i])
    i=i+1
while j < n:
    print(b[j])
    j=j+1
  



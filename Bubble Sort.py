n=int(input())
li=[int(i) for i in input().split()]
a=True
j=0
c0=0
while a:
    if sorted(li)==li:
        print("Array is sorted in",c0 ,"swaps.")
        print("First Element:",min(li))
        print("Last Element:",max(li))
        a=False 
    if li[j]>li[j+1]:
        li[j],li[j+1]=li[j+1],li[j]
        c0+=1
    if j==len(li)-2:
        j=0
    else:
        j+=1

    

n=int(input())
li=[int(i) for i in input().split()]
for j in range(len(li)-1):
    if li[j]>li[j+1]:
        li[j],li[j+1]=li[j+1],li[j]
        lif=li[:]
        lif[j]=lif[j+1]
        print(*lif)
        lil=li[:li.index(li[j])+1]
        for k in range(1,len(lil)):
            lif=li[:]
            if lil[-k]<lil[(-k)-1]:
                li[li.index(lil[-k])],li[li.index(lil[(-k)-1])]=li[li.index(lil[(-k)-1])],li[li.index(lil[-k])]
                lil[-k],lil[(-k)-1]=lil[(-k)-1],lil[-k]
                lif[li.index(lil[-k])]=lif[li.index(lil[(-k)-1])]
                print(*lif)
            else:
                break    
print(*li)



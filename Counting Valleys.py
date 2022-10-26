x=int(input())
y=input()
vall=0
al=0
for i in y:
    if i=="U":
        al+=1
        if al==0:
            vall+=1
    else:
        al-=1
print(vall)


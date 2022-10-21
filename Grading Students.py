x=int(input())
for i in range(x):
    y=int(input())
    if y >=38 :
        if (int(str(y)[0]+"5")-y)<3 and  (int(str(y)[0]+"5")-y)>0:
            print(int(str(y)[0]+"5"))
        elif (int(str(int(str(y)[0])+1)+"0")-y)<3 and  (int(str(int(str(y)[0])+1)+"0")-y)>0:
            print((int(str(int(str(y)[0])+1)+"0")))
        else:
            print(y)   
    else:
        print(y)

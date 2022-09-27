mylist=[]
try:
    n=int(input("enter length of list:"))
    for a in range(1,n+1):
        e=int(input("enter the element:"))
        mylist.append(e)
    print(mylist)
    i=len(mylist)
    prime=[]
    composite=[]
    for i in range(0,i):
        c=0
        for j in range(2,mylist[i]):
            if (mylist[i]%j==0):
                c=1
                break
        if (c==0):
            prime.append(mylist[i])
        else:
            composite.append(mylist[i])
    print("prime number list is ",prime)
    print("composite number list is ",composite)
    x=len(prime)
    print(x)
    y=len(composite)
    print(y)
except ValueError:
    print("enter integer number")

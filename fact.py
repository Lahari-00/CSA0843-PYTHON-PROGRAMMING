num=int(input("enter the num"))
factorial=1
if(num<0):
 print("factorial doesnot exists")
elif(num==0):
 print("factorial is 1")
else:
 for i in range(1,num+1):
  factorial=factorial*i
 print("facrtorial of num is",num,factorial)
        

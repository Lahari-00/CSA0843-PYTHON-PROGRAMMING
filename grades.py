print("enter the marks")
phy=int(input("enter the marks in physics"))
che=int(input("enter the marks in chemistry"))
maths=int(input("enter the marks in maths"))
total=phy+che+maths         
average=total/3
print("average is:",average)
if(average>=90):
    print("grade s")
elif(average>=80):
    print("grade a")
elif(average>=70):
    print("grade b")
elif(average>=60):
     print("grade c")
else:
     print("fail")

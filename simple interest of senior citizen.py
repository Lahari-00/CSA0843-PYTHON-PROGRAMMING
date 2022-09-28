p=int(input("enter the principle amount"))
t=int(input("enter the no.of year"))
y='yes'
n='no'
s=input("Is senior citizen")
if(s==y):
      r=12
      simple_interest=(p*t*12)/100
      print("simple interest is",simple_interest)
elif(s==n):
    r=10
    simple_interest=(p*t*10)/100
    print("simple interest is",simple_interest)
elif(p<0 or t<0):
    print("invalid input")


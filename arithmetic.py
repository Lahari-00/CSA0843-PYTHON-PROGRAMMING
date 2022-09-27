X=int(input("enter the first number"))
N=int(input("enter the second number"))
print(" 1 for power\n 2 for addition\n 3 for subtraction\n 4 for multiplication\n 5 for division")
choice=int(input("enter the choice"))
pow=X**N
add=X+N
sub=X-N
mul=X*N
div=X/N
if(choice==1):
    print("pow of X,N is:",pow)
elif(choice==2):
    print("add of X,N is:",add)
elif(choice==3):
    print("sub of X,N is:",sub)
elif(choice==4):
    print("mul of X,N is:",mul)
elif(choice==5):
    print("div of X,N is:",div)
else:
    print("invalid input")
           
                 
           

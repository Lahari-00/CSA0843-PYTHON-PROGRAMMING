import cmath
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
discriminant=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(discriminant))/(2*a)
root2=(-b+cmath.sqrt(discriminant))/(2*a)
print("root1 is ",root1)
print("root2 is ",root2)

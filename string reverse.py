string=input("enter the string")
if(string>='A' and string<='Z'):
    reverse_string=string[::-1]
    print("reverse string is",reverse_string)
elif(string>='a' and string<='z'):
    reverse_string=string[::-1]
    print("reverse string is",reverse_string)
else:
    print("invalid input")

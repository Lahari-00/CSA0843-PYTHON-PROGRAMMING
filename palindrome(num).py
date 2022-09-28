num=int(input("enter the number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
if(temp == reverse):
  print('true')
else:
  print("false")

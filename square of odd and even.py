num=int(input("enter the no.of elements"))
list=[]
for i in range(num):
   a=int(input("enter the elements"))
   list.append(a)
if(num<=0):
   print("INVALID INPUT")
else:
   def sumsquare(list):
      odd=0
      even=0
      for i in list:
          if i%2==0:
              even = even + i**2
          else:
              odd = odd + i**2
      list=[odd,even]
      return(list)
   print(sumsquare(list))

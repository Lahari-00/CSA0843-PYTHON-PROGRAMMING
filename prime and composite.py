a=[2,4,63,87,45,62,39,12,84,77]
prime_count=0
composite_count=0
prime_list=[]
composite_list=[]
for i in range(1,10):


    
  if(a[i]%j==0):
       composite_count=composite_count+1
       composite_list.append(a[i])
  else:
        prime_count=prime_count+1
        prime_list.append(a[i])
print("no.of prime numbers is:",prime_list)
print("no.of composite numbers are:",composite_list)

     


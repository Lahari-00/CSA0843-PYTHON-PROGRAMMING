random_list = [1,2,8,3,2,2,2,5,1]
frequency = {}
for item in random_list:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
print(frequency)

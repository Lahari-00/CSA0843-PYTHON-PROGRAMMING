year=int(input("enter the year"))
if(year<0):
    print("invalid input")
elif(year%4==0 or year%100!=0 or year%400==0):
    print("given year is a leap year")
    print("next leap is ",year+4)
else:
        print("not a leap year")
        for i in range(year-4,year):
            if(i%4==0):
                print("previous leap year",i)

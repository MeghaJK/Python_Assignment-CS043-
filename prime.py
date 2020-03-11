#prime number

start=int(input("enter the initial number"))
end=int(input("enter the end number"))
for val in range(start,end):
    if val>1:
        for n in range(2,val):
            if(val%n)==0:
                break
            else:
                print(val)
                break

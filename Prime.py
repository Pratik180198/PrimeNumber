num=int(input("Enter a number: "))
if num==1:
    print("It is not a Prime Number")
else:
    for i in range(2,num):
        if num%i==0:
            print("It is not a Prime Number")
            break
    else:
        print("It is a Prime Number")
n=int(input("enter the no"))
if(n>1):
    for i in range(1,n+1):
        if(n%i==0):
            print("The no is not prime no")
        else:
            print("The no is prime no")
            break

    
    

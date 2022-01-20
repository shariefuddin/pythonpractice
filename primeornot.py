
n=int(input("enter n value"));
if n>1:
 for i in range (2,n):
     if(n%i==0):
        print("given number is not prime");
        break;
 else:
         
    print("given number is  prime");
else:
    if n==1:
        print("given number is not prime");
    
         
n=int(input("enter number"));
sum=0;
for i in range(1,n):
    if(n%i)==0:
        sum=sum+i;
if sum==n:
    print("given number is perfect number");
else:
    print("given number is not perfect number");
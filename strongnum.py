n=int(input("enter n value"));
temp=n;
sum=0;
while(n):
    i=1;
    f=1;
    r=n%10;
    while(i<=r):
        f=f*i;
        i=i+1;
    sum=sum+f;
    n=n//10;
if sum==temp:
    print("given number is strong number");
else:
    print("given number is not strong number");
    
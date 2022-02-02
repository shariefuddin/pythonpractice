n=int(input("enter n value "))
temp = n;
sum=0;
for i in range(1,n+1):
    while(temp>0):
        fact=1;
        r=temp%10;
        for j in range(1,r+1):
            fact=fact*j;
            sum=sum+fact;
        temp=temp//10;
if sum==n:
    print(i,end=" ");
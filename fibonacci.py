n=int(input("enter n value"));
a=0;
b=1;
sum=0;
if n<=0:
    print("enter positive value");
elif n==1:
    print("fibonacci series for 1 is :",a);
else:
    print(a);
    print(b);
    for i in range(2,n):
        c=a+b;
        a=b;
        b=c;
        print(c);
  
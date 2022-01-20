n=int(input("enter number : "));
sum=0;
temp=n;
while temp>=0:
    digit=temp%10;
    sum += digit ** 3;
    temp //=10;
    if n == sum:
        print("given number is armstrong number");
        break;
    else:
        print("given number is not armstrong number");
        break;
    
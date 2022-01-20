amount=int(input("enter amount required to withdraw "));
print("tha amount you entered is : ",amount);
a=0;
b=0;
c=0;
if amount%100==0:
    if amount>=500:
        a=amount//500;
        amount=amount-(500*a);
        print("500 notes are : ",a);
    if amount>=200:
        b=amount//200;
        amount=amount-(200*b);
        print("200 notes are : ",b);
    if amount>=100:
        c=amount//100;
        print("100 notes are : ",c);
else:
    print("unable to withdraw choose another amount");
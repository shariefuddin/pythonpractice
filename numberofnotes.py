amount=int(input("enter amount requiresd to withdraw"));
a=0;
b=0;
c=0;
d=0;
e=0;
if amount%10==0:
    if amount>=200:
        a=amount//200;
        amount=amount-(200*a);
        print("200 notes are : ",a);
    if amount>=100:
        b=amount//100;
        amount=amount-(100*b);
        print("100 notes are : ",b);
    if amount>=50:
        c=amount//50;
        amount=amount-(50*c);
        print("50 notes are : ",c);
    if amount>=20:
        d=amount//20;
        amount=amount-(20*d);
        print("20 notes are : ",d);
    if amount>=10:
        e=amount//10;
        amount=amount-(10*e);
        print("10 notes are : ",e);
else:
    print("you entered invalid amount please enter amount ends with zero");

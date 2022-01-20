
p=int(input("enter principal amount"));
t=int(input("enter time"));
r=int(input("enter intrest rate amount"));
a=p*(pow(1+(r/100),t));
print("the final amount is :",a);
compound_intrest=a-p;
print("the compound number is : ",compound_intrest);

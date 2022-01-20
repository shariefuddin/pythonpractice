n1=int(input("enter number1 "));
n2=int(input("enter number2 "));
n3=int(input("enter number3 "));
print("given numbers are :",n1,n2,n3);
if(n1>n2)&(n1>n3):
    print("maximum nuber is :", n1);
elif(n2>n1)&(n2>n3):
    print("maximum number is : ", n2);
else:
    print("maximum number is : " ,n3);

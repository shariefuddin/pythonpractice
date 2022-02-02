num=int(input("enter number"));
ord=len(str(num));
sum=0;
temp=num;
while len(str(temp))>0:
    digit=temp%10;
    sum=sum+digit**ord;
    temp=temp//10;
    
if(num==sum):
    print("given number is armstrong number");
else:
    print("given number is not armstrong number");
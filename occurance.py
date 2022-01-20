count=0;
sum=0;
list=[23,45,56,23,23,90,77];
n=int(input("enter number"));
for i in list:
    if n==i:
        count=count+1;
       
if count!=0:
    sum=sum+count;
    print(sum);
else:
    print("mis match");
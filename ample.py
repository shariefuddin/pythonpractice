string=input("enter string ");
count=0;
i=0
j=len(string)
while string[i]==string[j-1] and i<=j:
    i=i+1
    j=j-1
    count=count+1

print(count)
if count-1==len(string)//2:
    print("Yes")
else:
    print("No")





#malayalam


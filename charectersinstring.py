string=input("enter any string ");
count=0;count1=0;count2=0;
for i in range(len(string)):
    if string[i].isalpha():
        count=count+1;
      
    elif string[i].isdigit():
        count1=count1+1;
       
    else:
        count2=count2+1;
       
print("number of alphabets are :",count);   
print("number of digits are :",count1);
print("number of special charecters in given string are :",count2);
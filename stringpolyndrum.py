string=input("enter string ");
count=0;
for i in range((len(string))):
  for j in range(i,len(string)):
      if string[i]==string[j-1]:
          count=count+1;
          j=j-1;
          if(i==j):
              break;
if count==len(string):
    print("given string is palindrome");
else:
    print("given number is not palindrome")
    
    

adda

malayalam


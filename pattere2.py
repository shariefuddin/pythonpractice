count=10;
odd=91;
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(count,end=" ");
            count=count+1;
     
        else:
            odd=odd-1;
            print(odd,end=" ");
    print();
basicsalary=int(input("enter basic salary "));
if basicsalary<10000:
    da=(basicsalary*70)/100;
    print("da is : ",da);
    hra=(basicsalary*65)/100;
    print("hra is :",hra);
elif 10000<basicsalary<20000:
    da=(basicsalary*75)/100;
    print("da is : ",da);
    hra=(basicsalary*73)/100;
    print("hra is :",hra);
else:
    da=(basicsalary*80)/100;
    print("da is : ",da);
    hra=(basicsalary*76)/100;
    print("hra is :",hra);
units=int(input("enter number of units "));
if units<=50:
    charge=(50*0.75);
    print("tha bill charge is : ",charge);
elif units<=150:
    charge=(50*0.75)+(units-50)*2.10;
    print("the bill charge is : ",charge);
elif units<=250:
    charge=(50*0.75)+(100*2.10)+(units-150)*2.50;
    print("the bill charge is : ",charge);
else:
    charge=(50*0.75)+(100*2.10)+(100*2.50)+(units-250)*2.80;
    print("the bill charge is : ",charge);
    
gst=(charge*10)/100;
charge=charge+gst;
print("total bill after adding gst is : ",charge);
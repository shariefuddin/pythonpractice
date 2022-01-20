project_marks=int(input("enter project marks"));
internal_marks=int(input("ente internal marks"));
external_marks=int(input("enter external marks"));

if project_marks&internal_marks&external_marks>=50:
    total_marks=((project_marks*70)/100)+((external_marks*20)/100)+((internal_marks*10)/100);
    print("total marks are :",total_marks);
    if total_marks>=90:
        print("A grade");
    elif total_marks>=75:
        print("B grade");
    elif total_marks>=50:
        print("C grade");
else:
    
    if project_marks<50:
        print("fail in project",project_marks);
    if internal_marks<50:
        print("fail in internal",internal_marks);
    if external_marks<50:
        print("fail in external ",external_marks);

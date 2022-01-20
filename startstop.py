start=int(input("enter start value"));
stop=int(input("enter stop value"));
if stop>start:
    for i in range(start,stop,1):
        print(i);
else:
    if  start>stop:
            for i in range(start,stop,-1):
                print(i);
       
r=float(input("enter radius of circle"));
l=int(input("enter length of the rectangle"));
b=int(input("enter berth of the rectangle"));
d=int(input("enter square side value"));
circle_area=M.pi*r*r;
circle_perimeter=2*M.pi*r;
rectangle_area=l*b;
rectangle_perimeter=2(l+b);
square_area=d*d;
square_perimeter=4*d;

print("the area and perimeter of circle are : ",circle_area,circle_perimeter);
print("the area and perimeter of rectangle are : ",rectangle_area,rectangle_perimeter);
print("the area and perimeter of square are : ",square_area,square_perimeter);

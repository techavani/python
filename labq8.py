a=float(input("enter side 1"))
b=float(input("enter side 2"))
c=float(input("enter side 3"))
sides=sorted({a,b,c})
if(sides[2]**2 == sides[0]**2 + sides[1]**2):
    print("it is a right angled troangle")
else:
    print("not a  right angledtriangle")
test1=float(input("enter marks for test 1"))
test2=float(input("enter marks for test 2"))
test3=float(input("enter marks for test 3"))
if(test1>=test3 and test2>=test3):
    print((test1+test2)/2)
elif(test2>=test1 and test3>=test1):
    print((test2+test3)/2)
else:
    print((test1+test2)/2)

a = int(input("first number"))
s = input("symbol")
b = int(input("second number"))
if s=="-":
    print (a-b)
elif s=="+":
    print(a+b)
elif s=="*":
    print(a*b)
elif s=="/":
    print(a/b)
else:
    print("error")



a = int(input("enter a number"))
if a>=100000 and a<1000000 :
    s = str(a)
    s1= s[:3]
    s2= s[3:]
    sum1 = 0
    sum2 = 0
    for i in s1:
        sum1 = sum1 + int(i)
    for i in s2:
        sum2 = sum2 + int(i)
    if sum1==sum2:
        print("yes")
    else:
        print("no")
else:
    print ("error")
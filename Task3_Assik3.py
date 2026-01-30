s = input()

if s[4] == 'x':
    num1 = int(s[0])
    num2 = int(s[2])
    if s[1] == '+':
        print(num1 + num2)
    else:
        print(num1 - num2)

elif s[0] == 'x':
    num2 = int(s[2])
    res = int(s[4])
    if s[1] == '+':
        print(res - num2)
    else:
        print(res + num2)

elif s[2] == 'x':
    num1 = int(s[0])
    res = int(s[4])
    if s[1] == '+':
        print(res - num1)
    else:
        print(num1 - res)
enter = input('Enter: ').replace(' ','')
x = 0
y = 0
z = 0
v1 = 0
lst = []
for i in enter:
    if ord(i) < 48:
        lst.append(i)

if len(lst) == 1:
    x = int(enter[:enter.index(lst[0])])
    y = int(enter[(enter.index(lst[0]))+1:])
if len(lst) == 2:
    if lst[0] == '*' or lst[0] == '/':
        x = int(enter[:enter.index(lst[0])])
        y = int(enter[(enter.index(lst[0])) + 1: (enter.rindex(lst[1]))])
        z = int(enter[(enter.rindex(lst[1]))+1:])
    elif lst[1] == '*' or lst[1] == '/' :
        if lst[0] == '+':
            z = int(enter[:enter.index(lst[0])])
            x = int(enter[(enter.index(lst[0])) + 1: (enter.rindex(lst[1]))])
            y = int(enter[(enter.rindex(lst[1])) + 1:])
            lst.reverse()
        elif lst[0] == '-':
            z = -int(enter[:enter.index(lst[0])])
            x = -int(enter[(enter.index(lst[0])) + 1: (enter.rindex(lst[1]))])
            y = int(enter[(enter.rindex(lst[1])) + 1:])
            lst.reverse()
    else:
        x = int(enter[:enter.index(lst[0])])
        y = int(enter[(enter.index(lst[0])) + 1: (enter.rindex(lst[1]))])
        z = int(enter[(enter.rindex(lst[1])) + 1:])

if lst[0] == '+':
    v1 = x + y
    if len(lst) == 1:
        print(v1)
elif lst[0] == '-':
    v1 = x - y
    if len(lst) == 1:
        print(v1)
elif lst[0] == '*':
    v1 = x * y
    if len(lst) == 1:
        print(v1)
elif lst[0] == '/':
    v1 = x / y
    if len(lst) == 1:
        print('%.2f' % v1)

if len(lst) == 2:
    if lst[1] == '+' and v1 != 0:
        print(v1 + z)
    elif lst[1] == '-' and v1 != 0:
        print( v1 - z)
    elif lst[1] == '*' and v1 != 0:
        print(v1 * z)
    elif lst[1] == '/' and v1 != 0:
        print(v1 / z)
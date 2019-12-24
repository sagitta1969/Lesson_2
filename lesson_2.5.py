a =  [7, 5, 3, 3, 2]
#b = 0
b = int(input("введите положительное число: "))
if b > max(a):
    a.insert(0, b)
    print(a)
elif b < min(a):
    a.append(b)
    print(a)
else:
    d = [b]
    for item in a:
        if item >= b:
            d.insert(-1, item)
        elif item < b:
            d.append(item)
    print(d)
#я не  знаю как и что я сделал

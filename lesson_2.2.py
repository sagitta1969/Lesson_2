a = input("введите значения списка: ")
a = list(a)
i = len(a)
if i % 2 != 0:
    c = list(a[-1])
    a.pop()
    a[::2], a[1::2] = a[1::2], a[::2]
    a = a + c
    print(a)
else:
    a[::2], a[1::2] = a[1::2], a[::2]
    print(a)

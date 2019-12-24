a = input("введите текстовую строку: ")
a = list(a.split())
b = 0
for i in a:
    b = b + 1
    print(b, str(i[0:9]))

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

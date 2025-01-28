a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

result = []

if 1 <= a <= 3:
    result.append(a)
if 1 <= b <= 3:
    result.append(b)
if 1 <= c <= 3:
    result.append(c)

print("Числа, принадлежащие интервалу [1, 3]:", result)

impor
x = -2.235e-2
y = 2.23
z = 15.221
part1 = (math.exp(x - y) * abs(x - y)) / ((x + y) * (math.atan(x) + math.atan(z)))
part2 = math.pow(abs(x), 1/6)
part3 = math.log(y) ** 2
s = part1 + part2 + part3
print(f"Значение s: {s:.5f}")

import math
# x = u0 умножить t умножить cos(a)
# y = u0 умножить t sin(a) - gt2 / 2

u = input("Введите начальную скорость тела (Vнач.): ")
t = input("Введите время полёта тела (t): ")
a = input("Введите угол под которым бросили тело (*): ")
g = 9.8

# перевод из градусов в радианы
a = float(a) * math.pi
a = float(a) / 180

# нахождение координаты x
x = float(u) * float(t) * math.cos(a)

# нахождение координаты y
m = float(u) * float(t) * math.sin(float(a))
n = float(g) * float(t) * float(t)
b = float(n) / 2
y = float(m) - float(b)

print("\n")
print("Значение высоты тела: " + str(y))
print("Значение дальности полёта тела: " + str(x))
print("\n")
k = input("Ставьте 5 пж)")
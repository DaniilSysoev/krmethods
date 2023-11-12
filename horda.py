# f(x) = ln(x) + x - 2 = 0
import math


def f(x):
    return math.log(x) + x - 2


def f1(x):
    return 1/x + 1


def f2(x):
    return -1/x**2


a = 1
b = 2
x = 0
eps = 0.001


eps = 0.001
# проверка на сходимость сначала a, потом b
if f(a)*f2(a) > 0:
    x = a
elif f(b)*f2(b) > 0:
    x = b
else:
    print("Нет сходимости")
    exit()

x1 = 2
i = 1
while True:
    x2 = x1 - (x1-x)/(f(x1)-f(x))*(f(x1))
    print(f"Итерация {i}")
    print(f"x = {x}, x1 = {x1}, x2 = {x2} abs(x2-x1) = {abs(x2-x1)}\n")
    if abs(x2-x1) < eps:
        break
    x = x1
    x1 = x2
    i += 1
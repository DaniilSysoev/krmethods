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
# проверка на сходимость сначала a, потом b
if f(a)*f2(a) > 0:
    x = a
elif f(b)*f2(b) > 0:
    x = b
else:
    print("Нет сходимости")
    exit()

i = 1
while True:
    print(f"Итерация {i}")
    print(f"x = {x}, f(x) = {f(x)}, abs(f(x)) = {abs(f(x))}\n")
    if abs(f(x)) < eps:
        break
    x = x - f(x)/f1(x)
    i += 1
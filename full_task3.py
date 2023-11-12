# функция приведения матрицы к верхнетреугольному виду методом Гаусса с выводом промежуточных результатов
# возвращает матрицу в верхнетреугольном виде

# нумпай чисто для красивого вывода матриц
import numpy as np

# это получение верхнетреугольной, нижнетреугольной и вектора b методом гаусса
def gauss(A):
    U = A[:]
    n = len(U)
    m = len(U[0])
    # сделать матрицу с единичной диагональю
    L = [[0] * n for i in range(n)]
    for i in range(n):
        L[i][i] = 1
    for k in range(n):
        for i in range(k + 1, n):
            c = -U[i][k] / U[k][k]
            L[i][k] = -c
            for j in range(k, m):
                U[i][j] += c * U[k][j]
        # вывод каждого этапа получения верхнетреугольной матрицы
        #print(np.matrix(U))
        #print()
    b = [0] * n
    for i in range(n):
        b[i] = U[i][m - 1]
    
    # удалить последний столбец U
    for i in range(n):
        U[i].pop()
    return U, L, b

# перемножение матриц для проверки
def mult(A, B):
    n = len(A)
    m = len(B[0])
    C = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

# функция определитель матрицы из U
def det(U):
    d = 1
    for i in range(len(U)):
        d *= U[i][i]
    return d

# функция решения системы Ux = b
def solve(U, b):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += U[i][j] * x[j]
        x[i] = (b[i] - s) / U[i][i]
    return x

# здесь указать изначальную матрицу с входящим в нее столбцом b
A = [[2, 2, -1, 1, 4],
     [4, 3, -1, 2, 6],
     [8, 5, -3, 4, 12],
     [3, 3, -2, 2, 6]]

U, L, b = gauss(A)

print("U = ")
print(np.matrix(U))
print("L = ")
print(np.matrix(L))
print("b = ")
print(np.matrix(b))
print()

# проверка решения
#print("A = ")
#print(np.matrix(A))
#print("L*U = ")
#print(np.matrix(mult(L, U)))

print("det(A) = ", det(U))
print()

x = solve(U, b)
print("x = ", x)
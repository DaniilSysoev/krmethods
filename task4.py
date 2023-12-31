#4x1+2x2+x3=25
#2x1+4x2+x3=27
#x1+x2+3x3=22
import numpy as np

# каноническая формула для решения слау методом простой итерации
# x_i = (b_i - sum(a_ij*x_j))/a_ii


A = [[4, 2, 1, 25], [2, 4, 1, 27], [1, 1, 3, 22]]
eps = 0.05
w = 1.5
mode = 1 # метод простой итерации
#mode = 2 # метод зейделя
#mode = 3 # метод верхней релаксации

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

# метод простой итерации для решения слау
def func(A, x, t, mode):
    t += 1
    print(f"Итерация {t}")
    # проверить, что значения на главной диагонали больше чем сумма остальных элементов в строке
    for i in range(len(A)):
        if abs(A[i][i]) <= sum([abs(A[i][j]) for j in range(len(A)) if j != i]):
            print("Не сходится")
            exit()
    # получить матрицу начального приближения
    x = x
    xi = [0] * len(A)
    # метод итерации
    if mode == 1:
        xi[0] = (A[0][len(A)]-A[0][1]*x[1]-A[0][2]*x[2])/A[0][0]
        xi[1] = (A[1][len(A)]-A[1][0]*x[0]-A[1][2]*x[2])/A[1][1]
        xi[2] = (A[2][len(A)]-A[2][0]*x[0]-A[2][1]*x[1])/A[2][2]
    # метод зейделя
    elif mode == 2:
        xi[0] = (A[0][len(A)]-A[0][1]*x[1]-A[0][2]*x[2])/A[0][0]
        xi[1] = (A[1][len(A)]-A[1][0]*xi[0]-A[1][2]*x[2])/A[1][1]
        xi[2] = (A[2][len(A)]-A[2][0]*xi[0]-A[2][1]*xi[1])/A[2][2]
    # метод верхней релаксации
    elif mode == 3:
        xi[0] = (1-w)*x[0]+w*(A[0][len(A)]-A[0][1]*x[1]-A[0][2]*x[2])/A[0][0]
        xi[1] = (1-w)*x[1]+w*(A[1][len(A)]-A[1][0]*xi[0]-A[1][2]*x[2])/A[1][1]
        xi[2] = (1-w)*x[2]+w*(A[2][len(A)]-A[2][0]*xi[0]-A[2][1]*xi[1])/A[2][2]



    # вывести полученную матрицу
    print(np.matrix(xi))
    print()
    # получить матрицу для проверки сходимости
    B = [0] * len(A)
    flag = 0
    for i in range(len(A)):
        # проверка по невязке
        B[i] = abs(sum([A[i][j] * xi[j] for j in range(len(A))]) - A[i][len(A)])
        #B[i] = abs(mult(A[i], xi[i]))
        if B[i] > eps:
            flag = 1
    # вывести матрицу для проверки сходимости
    print(np.matrix(B))
    print()
    # если хотя бы одно значение больше eps, то продолжить итерации
    if flag:
        x = xi[:]
        func(A, x, t, mode)
    else:
        print("Решение:")
        print(np.matrix(xi))

x = [0] * len(A)
t = 0
func(A, x, t, mode)
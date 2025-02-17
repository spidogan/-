#Программная реализация подсчёта определителя квадратной матрицы методом Крамера, с рекурсивным методом подсчёта определителей.
import random
import time

def show(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

def create_matrix(n):
    return [[random.randint(1, 5) for _ in range(0, n)] for _ in range(0, n)]

def determinant(matrix):
    n = len(matrix)
    return matrix[0][0] if n == 1 else sum([((-1)**j) * matrix[0][j] * determinant([row[:j] + row[j + 1:] for row in matrix[1:]]) for j in range(0, n)])
    
def create_vec_x(n):
    return [random.randint(1, 5) for _ in range(0, n)]

def multiplication(matrix, column):
    n = len(matrix)
    return [sum([row[i] * column[i] for i in range(0, n)]) for row in matrix]

def Kramer(matrix, f, det):
    n = len(f)
    return [determinant([[matrix[i][j] if j != k else f[i] for j in range(0, n)] for i in range(0, n)]) // det for k in range(0, n)]

print("Введите размер квадратной матрицы")
n = int(input())
matrix = create_matrix(n)
det = determinant(matrix)
while det  == 0:
    matrix = create_matrix(n)
    det = determinant(matrix)
print(f"Матрица A {n} x {n}:")
show(matrix)
print("Определитель:")
print(det)
print("X:")
X = create_vec_x(n)
print(*X)
print("f:")
f = multiplication(matrix, X)
print(*f)
print('Метод решения - Крамер')
t1 = time.perf_counter()
print(*Kramer(matrix, f, det))
print(time.perf_counter() - t1)

import numpy as np


# 算数运算
def fun1():
    print("=======================算数运算=================================")
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 4.0, 6.0])
    print(type(x))
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)


fun1()


# N维数组
def fun2():
    print("=======================N维数组=================================")
    A = np.array([[1, 2], [3, 4]])
    print(A)
    print(A.shape)
    print(A.dtype)

    B = np.array([[3, 0], [0, 6]])
    print("A+B:", A + B)
    print("A-B:", A - B)
    print("A*B:", A * B)
    print("A/B:", A / B)


fun2()


def func3():
    print("=======================广播=================================")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([10, 20])
    print("A*10", A * 10)
    print("A*B", A * B)
    print("B*A", B * A)


func3()


def func4():
    print("=======================访问元素=================================")
    X = np.array([[51, 55], [14, 19], [0, 4]])
    print("X[0]", X[0])
    print("X[0][1]", X[0][1])
    for row in X:
        for r in row:
            print(r)
    # 转换成一维数组
    X = X.flatten()
    print(X > 15)
    print(X[X > 15])


func4()


def func5():
    x = np.array([[[5, 6], [7, 8]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]])
    print(x)
    print(x.shape)


func5()

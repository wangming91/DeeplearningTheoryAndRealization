import numpy as np
import matplotlib.pyplot as plt


def func1():
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    # print(x)
    # print(y)

    #     绘制图形
    plt.plot(x, y)
    plt.show()


func1()


def func2():
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # 绘制图形
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="cos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("x & y")
    plt.legend()
    plt.show()


func2()

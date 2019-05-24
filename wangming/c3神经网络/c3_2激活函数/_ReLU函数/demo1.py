# 到目前为止，我们介绍了作为激活函数的阶跃函数和sigmoid函数。在
# 神经网络发展的历史上，sigmoid函数很早就开始被使用了，而最近则主要
# 使用ReLU（Rectified Linear Unit）函数。
# ReLU函数在输入大于0时，直接输出该值；在输入小于等于0时，输
# 出0

import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


def show():
    x = np.arange(-5, 5, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-1, 6.1)
    plt.show()


show()

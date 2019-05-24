import wangming.c3神经网络.c3_2激活函数._阶跃函数.demo1 as demo1
import numpy as np
import matplotlib.pyplot as plt

d = demo1.Demo1()
x = np.arange(-5.0, 5.0, 0.1)
y = d.func3(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

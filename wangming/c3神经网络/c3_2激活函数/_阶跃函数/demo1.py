import numpy as np


class Demo1:
    # 阶跃函数版本1
    def func1(self, x):
        if x > 0:
            return 1
        else:
            return 0

    # 阶跃函数版本2,可考虑使用numpy
    def func2(self, x):
        y = x > 0
        return y.astype(np.int)

    def func3(self, x):
        return np.array(x > 0, dtype=np.int)

    # 对func2的说明
    def explainFunc2(self):
        x = np.array([-1, 1, 2])
        print(x)
        y = x > 0
        print(y)
        z = y.astype(np.int)
        print(z)
        # [-1  1  2]
        # [False  True  True]
        # [0 1 1]

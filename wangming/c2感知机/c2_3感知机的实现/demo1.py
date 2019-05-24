import numpy as np


class Demo1():
    # 与门实现
    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        temp = np.sum(x * w) + b
        if temp <= 0:
            return 0
        else:
            return 1

    # 非门实现
    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        temp = np.sum(x * w) + b
        if temp <= 0:
            return 0
        else:
            return 1

    # 或门实现
    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.2
        temp = np.sum(x * w) + b
        if temp <= 0:
            return 0
        else:
            return 1

    # 异或
    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)
        y = self.AND(s1, s2)
        return y


d = Demo1()
print(d.XOR(0, 0))  # 输出0
print(d.XOR(1, 0))  # 输出1
print(d.XOR(0, 1))  # 输出1
print(d.XOR(1, 1))  # 输出0

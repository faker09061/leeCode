import numpy as np
import matplotlib.pyplot as plt
import math

# x, y 的参数方程，用来计算在某个时间进度下，x和y的坐标
def fx(t):
    x = 2 * np.cos(t) - np.cos(2*t)
    return x
def fy(t):
    y = 2* np.sin(t) - np.sin(2*t)
    return y


def ft(t):
    x = fx(t)
    y = fy(t)
    return x + 1j * y


t= np.linspace(0, 2 * math.pi, 100)

x = fx(t)

y = fy(t)

# 查看原始数据
plt.title('the origin data')
plt.plot(x, y, c = 'blue')
# plt.show()


# 微分计算的步长
dx = 0.001

# 计算定积分, dx是微分程度， left， right是上下界
def calF(f, dx, left, right):
    Sum = 0


    # 选值进行计算的点
    xNum = np.linspace(left, right, int((right-left) /dx))

    for i in xNum:
        now = f(i) * dx
        Sum += now
    return Sum


tmpf = lambda x: x**2

ans = calF(tmpf, dx, 0, 1)
print(ans)


T = 2 * math.pi
wo = 2 * math.pi / T

# 这里用得是欧拉公式化简后的 e 的指数形式
c = []


# 这里的范围就相当于是圈数
for i in range(0,6):
    print(i)
    tmpf = lambda x: ft(x)* np.exp(-1j * i * wo * x)  # 隐函数表达式

    nowc = calF(tmpf, dx, 0, T) / T  # 定积分计算， 因为具有着正交的性质
    c.append([i, nowc])


print(c)


# 计算傅里叶级数的函数
def FinallFunc(t):
    Sum = 0
    for n, nowc in c:
        tmp = nowc * np.exp(1j * n * wo * t)
        Sum += tmp

    return Sum



# 进行测试， 看是否计算出来了傅里叶级数
tx = []
ty = []
for i in t:
    num = FinallFunc(i)
    tx0 = num.real
    ty0 = num.imag

    tx.append(tx0)
    ty.append(ty0)
plt.title('the Fourier data')
plt.scatter(tx, ty, c= 'black')
plt.show()


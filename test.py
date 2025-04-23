import numpy as np
import matplotlib.pyplot as plt

# 作图工具包
# 1. 导入numpy和matplotlib.pyplot模块
t = np.arange(0, 15, 0.2)
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^", t, 2**t, "y*")
plt.show()

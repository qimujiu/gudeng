# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 09:58:50 2025

@author: lenovo
"""
import numpy as np
import matplotlib.pyplot as plt

# 参数设置
L = 2.5e9  # 卫星间距，单位：米
c = 3e8    # 光速，单位：m/s

# 频率范围（1e-5 Hz 到 1 Hz）
f = np.logspace(-5, 0, 1000)
omega = 2 * np.pi * f

# 计算无量纲项 omega*L/c
term = omega * L / c

# 计算平均响应（公式来自文献(40)）
response = (4 * term)**2 * (np.sin(term))**2 * (2 * np.sin(2 * term))**2 * (3/20)

# 绘图
plt.figure(figsize=(12, 8))
plt.loglog(f, response, label='Average GW Response (X2.0)', color='blue')
plt.xlabel('Frequency [Hz]', fontsize=12)
plt.ylabel(r'$\langle R_{L,X_{2.0}} \rangle$', fontsize=12)
plt.title('LISA TDI-X2.0 Average Gravitational Wave Response', fontsize=14)
plt.grid(True)
plt.legend()
plt.xlim(1e-5, 1)
plt.show()
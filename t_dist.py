# -*- coding: utf-8 -*-
"""T-dist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UfqL51VYfKBGjLF68v4xwGcUIsp43UoT
"""

import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

df= 2.7
m, v, s, k = t.stats(df, moments='mvsk')
x = np.linspace(t.ppf(0.01, df),t.ppf(0.99, df), 100)

fig, ax = plt.subplots(1, 1)
ax.plot(x, t.pdf(x, df),
       'r-', lw=5, alpha=0.6, label='t pdf')


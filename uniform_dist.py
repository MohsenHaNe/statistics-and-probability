# -*- coding: utf-8 -*-
"""uniform-dist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UfqL51VYfKBGjLF68v4xwGcUIsp43UoT
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0,1,1000)
count, bins, ignored = plt.hist(x, 50)

plt.plot(bins, np.ones_like(bins), linewidth=2, color='b')
plt.show()


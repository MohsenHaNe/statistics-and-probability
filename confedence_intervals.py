# -*- coding: utf-8 -*-
"""confedence_intervals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s8pEWbvso7Xx1xLL771w0NuM2OxWhHPI
"""

import numpy as np
import scipy.stats as st

data = np.random.randint(1, 100, 1000)

intervals = st.norm.interval(confidence=0.95,loc=np.mean(data),scale=st.sem(data))

def confedence_intervals(sample,confidence):
  mean = np.mean(sample)
  scale = st.sem(sample)
  limits = st.norm.interval(confidence=confidence,loc=mean,scale=scale)
  return limits

confedence_intervals(data,0.95)


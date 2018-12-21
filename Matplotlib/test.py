import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(0.0,5.0,0.02)
y=np.exp(-x)*np.cos(2*np.pi*x)
plt.plot(x,y)
plt.grid(color='gray')
plt.show()
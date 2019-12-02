#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes()
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
y=3*x-30000
ax.plt(x, y) 





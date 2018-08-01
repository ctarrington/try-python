# jupyter notebook must be running
# vs code integration allows cell to be run

# %%
import matplotlib.pyplot as plt
import numpy as np

from bokeh.io import show, output_notebook
from bokeh.plotting import figure

from IPython.display import display

import seaborn as sns

# %%
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# %%
output_notebook()

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Legend Example", tools=TOOLS)
p1.circle(x, y, legend="sin(x)")
p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend="3*sin(x)", color="green")
show(p1)

# %%
tips = sns.load_dataset('tips')
display(tips)

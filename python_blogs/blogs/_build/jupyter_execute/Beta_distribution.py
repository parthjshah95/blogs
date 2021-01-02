#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.stats import beta
import plotly.graph_objs as go
import numpy as np
from ipywidgets import interact

# fig, ax = plt.subplots(1, 1)
# a, b = 2.31, 0.627
# x = np.linspace(beta.ppf(0.01, a, b),
#                 beta.ppf(0.99, a, b), 100)
# ax.plot(x, beta.pdf(x, a, b),
#        'r-', lw=5, alpha=0.6, label='beta pdf')
# plt.show()


# In[2]:


fig = go.FigureWidget()
fig.add_scatter()
scatt = fig.data[0]
fig.update_layout(
    width = 800,
    height = 500,
)
fig.update_xaxes(range=[0, 1])


@interact(a=(0, 10, 0.01), b=(0, 10, 0.01))
def update(a=2, b=2):
    with fig.batch_update():
        x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
        scatt.x = x
        scatt.y = beta.pdf(x, a, b)
fig


# In[ ]:





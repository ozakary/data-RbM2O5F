#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

# Function to convert the slope value to scientific format 
def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))

data_1 = np.loadtxt("figure_S1-a_data.txt", skiprows = 1, usecols=(1, 2))

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(data_1[:6, 0], data_1[:6, 1], '.', color = '#2A9D8F', ms = 22, mec = '#2A9D8F')
ax.plot(data_1[6, 0], data_1[6, 1], '.', color = '#E76F51', ms = 22, mec = '#E76F51')

ax.set_xlabel(r'$\sigma$$_{iso}$ / ppm')#, fontsize = 22)
ax.set_ylabel(r'$\delta$$_{iso}$ /ppm')#, fontsize = 22)

ax.set_xlim(-200, 300)
ax.set_ylim(-200, 300)

# Establishing the linear regression

# DATA n°1

# Definnig the regression variables (x, y)
x1 = data_1[:, 0]
y11 = data_1[:, 1]

# Calculating the linear regression model
model11 = sm.OLS(y11, sm.add_constant(x1))
results11 = model11.fit()

# extract intercept b and slope m
b11, m11 = results11.params

# plot y = m*x + b
ax.axline(xy1=(0, b11), slope = m11, linestyle='-', color='#264653', linewidth=2)

text = [r'$\delta$$_{iso}$', r'$\sigma$$_{iso}$']
# Adding text referring to the slope = thermal expansion coefficient and the R-squared value
ax.text(x = -190, y = -150, s = text[0] + "$= {m:.3f}$".format(m=m11) + '$(29)$ ' + text[1] + ' $+$ ' + "${b:.1f}$".format(b=b11) + '$(4.3)$', color = '#264653', fontsize = 14.5)
ax.text(x = -30, y = -190, s = f'$R^2 = {results11.rsquared:.4f}$', color = '#264653', fontsize = 14.5)


# Show plot
plt.tight_layout()
fig.savefig('19F_iso_slop_RbNb2O5F.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()

#print(results11.summary())

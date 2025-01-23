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

data_1 = np.loadtxt("figure_S3_data.txt", skiprows = 1, usecols=(2, 3))

fig, ax = plt.subplots(figsize=(6, 6))

# Plotting DATA
ax.plot(data_1[0, 0], data_1[0, 1], '.', color = '#2A9D8F', ms = 14, mec = '#2A9D8F')
ax.plot(data_1[1:4, 0], data_1[1:4, 1], 's', color = '#2A9D8F', ms = 6, mec = '#2A9D8F')
ax.plot(data_1[4, 0], data_1[4, 1], '*', color = '#2A9D8F', ms = 10, mec = '#2A9D8F')
ax.plot(data_1[5, 0], data_1[5, 1], 'D', color = '#2A9D8F', ms = 6, mec = '#2A9D8F')
ax.plot(data_1[6, 0], data_1[6, 1], 'v', color = '#2A9D8F', ms = 8, mec = '#2A9D8F')
ax.plot(data_1[7:9, 0], data_1[7:9, 1], 'P', color = '#2A9D8F', ms = 10, mec = '#2A9D8F')
ax.plot(data_1[9, 0], data_1[9, 1], '^', color = '#2A9D8F', ms = 8, mec = '#2A9D8F')

ax.set_xlabel(r'$\sigma$$_{iso}$ / ppm')#, fontsize = 22)
ax.set_ylabel(r'$\delta$$_{iso}$ /ppm')#, fontsize = 22)

ax.set_xlim(3050, 3250)
ax.set_ylim(-60, 80)

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
ax.text(x = 3060, y = 70, s = text[0] + "$= {m:.3f}$".format(m=m11) + '$(32)$ ' + text[1] + ' $+$ ' + "${b:.0f}$".format(b=b11) + '$(103)$', color = '#264653', fontsize = 14.5)
ax.text(x = 3120, y = 60, s = f'$R^2 = {results11.rsquared:.4f}$', color = '#264653', fontsize = 14.5)

ax.legend(['RbF', 'RbNO$_3$', 'RbVO$_3$', 'RbClO$_4$', 'RbLaF$_4$', 'Rb$_2$SO$_4$', 'RbSr$_2$Nb$_3$O$_{10}$'], loc = 'lower left', frameon=False)#fontsize = 14, markerscale = 1.5)

# Show plot
plt.tight_layout()
fig.savefig('87Rb_iso_slope.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()

#print(results11.summary())

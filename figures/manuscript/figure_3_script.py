#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
matplotlib.use('tkagg')  # Use the TkAgg backend (change to another backend if needed)
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional


# plt.style.use("default") # set the plot style
# plt.rcParams["font.family"] = "serif" # To globaly change the font POLICE
# plt.rcParams["mathtext.fontset"] = "stix"

#colors = ['#264653', '#2A9D8F', '#E9C46A', '#E76F51', '#F3B6A5']

data_1 = np.loadtxt("figure_3_data-1.xyn", skiprows=2)
data_2 = np.loadtxt("figure_3_data-2.xyn", skiprows=2)

fig, ax = plt.subplots(1, figsize=(6, 6))

ax.scatter(data_1[:, 0], data_1[:, 1]-5000, marker='o', s=50, edgecolors='red', linewidths=1, color='none', alpha=1, label='Experimental')
ax.plot(data_1[:, 3], data_1[:, 4]-5000, color='#264653', linewidth=0.8, label='Calculated')
ax.plot(data_1[:, 6], data_1[:, 7]+10000, color='grey', linewidth=0.8, label=r'$\Delta_{model}$')
ax.scatter(data_1[:, 9], data_1[:, 10]+10000, marker='|', s=50, edgecolors='none', linewidths=1, color='#2A9D8F', alpha=1, label='Bragg positions')

ax.scatter(data_2[:, 0], data_2[:, 1]+185000, marker='o', s=50, edgecolors='red', linewidths=1, color='none', alpha=1)
ax.plot(data_2[:, 3], data_2[:, 4]+185000, color='#264653', linewidth=0.8)
ax.plot(data_2[:, 6], data_2[:, 7]+200000, color='grey', linewidth=0.8)
ax.scatter(data_2[:, 9], data_2[:, 10]+190000, marker='|', s=50, edgecolors='none', linewidths=1, color='#2A9D8F', alpha=1)

ax.set_xlim(5,120)

ax.set_xlabel(r'$2\theta$ / $deg$', fontsize=16)
ax.set_ylabel(r'$Intensity$ / $a.u.$', fontsize=16)

ax.text(x = 90, y = 40000, s = r'RbNb$_{2}$O$_{5}$F', color = 'k', fontsize = 16)
ax.text(x = 90, y = 230000, s = r'RbTa$_{2}$O$_{5}$F', color = 'k', fontsize = 16)

ax.legend(frameon=False)

fig.savefig('XRPD_diagrams.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()

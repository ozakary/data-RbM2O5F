#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

# Load the data
data_1 = pd.read_csv("./step-2_OF_dist/concatenated_configs_RbX18_l.csv")
data_2 = pd.read_csv("./step-2_OF_dist/concatenated_configs_RbX18_h.csv")
data_3 = np.loadtxt("./Rb_anionic-environements_vf-all_publi.txt", skiprows=1, usecols=range(1, 19 + 1))

# Sum the data from column 3 to the end
column_sum_1 = np.sum(data_1.iloc[:, 2:], axis=0)
column_sum_2 = np.sum(data_2.iloc[:, 2:], axis=0)

# Calculate the denominator
denom_1 = 100 / np.sum(column_sum_1)
denom_2 = 100 / np.sum(column_sum_2)

# Calculate the probabilities
Prob_th_1 = column_sum_1 * denom_1
Prob_th_2 = column_sum_2 * denom_2

column_sum_3 = []
Prob_th_3 = []
for i in range(len(data_3[0, :])):
    column_sum_3.append(np.sum(data_3[:, i]))
denom = 100 / np.sum(column_sum_3)
for i in range(len(column_sum_3)):
    Prob_th_3.append(column_sum_3[i] * denom)

def Proba_conf(n):
    p = np.arange(0, n+1, 1)
    k = np.arange(n, -1, -1)
    Comb1 = []
    for i in range(len(p)):
        Comb = (np.math.factorial(n))/(np.math.factorial(p[i])*np.math.factorial(n - p[i]))
        Comb1.append(Comb)
    Proba = Comb1*((5/6)**k)*((1/6)**p)
    return Proba*100

# Set up parameters for the bar plot
n_groups = len(Prob_th_1)  # Adjust to the number of groups

index = np.arange(n_groups)

bar_width = 0.2
opacity = 0.25

fig, ax = plt.subplots(figsize=(4.5, 5.5))

# Plot the first probability with a starting point of 0
bar_plot_11 = ax.bar(index[:7] - bar_width, np.array(Prob_th_1)[:7] / 100, bar_width, color='#264653', alpha=1, bottom=0, label=r'$N_{select}\{E_{Ewald}^{(\searrow)}\}$')
bar_plot_12 = ax.bar(index[8] - bar_width, np.array(Prob_th_1)[-1] / 100, bar_width, color='#264653', alpha=1, bottom=0)

bar_plot_21 = ax.bar(index[:7], np.array(Prob_th_2)[:7] / 100, bar_width, color='#2A9D8F', alpha=1, bottom=0, label=r'$N_{select}\{E_{Ewald}^{(\nearrow)}\}$')
bar_plot_22 = ax.bar(index[8], np.array(Prob_th_2)[-1] / 100, bar_width, color='#2A9D8F', alpha=1, bottom=0)

bar_plot_31 = ax.bar(index[:7] + bar_width, Proba_conf(18)[:7] / 100, bar_width, color='#E76F51', alpha=1, label='Formula')
bar_plot_32 = ax.bar(index[8] + bar_width, Proba_conf(18)[-1] / 100, bar_width, color='#E76F51', alpha=1)

bar_plot_41 = ax.bar(index[:7] + 2 * bar_width, np.array(Prob_th_3)[:7] / 100, bar_width, color='#F3B6A5', alpha=1, bottom=0, label=r'Selected')
bar_plot_42 = ax.bar(index[8] + 2 * bar_width, np.array(Prob_th_3)[-1] / 100, bar_width, color='#F3B6A5', alpha=1, bottom=0)

x_ticks_labels=['0', '1', '2', '3', '4', '5', '6', '...', '18']
x_ticks=list(index[:8] + bar_width *0.55) + [index[8] + bar_width *0.5]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticks_labels)


ax.set_ylim(0, 1)
ax.set_xlabel(r'$y$ in $[RbO_{18-y}F_{y}]^{m-}$', fontsize=18)
ax.set_ylabel(r'$P(y)$', fontsize=18)

print(Prob_th_2)

plt.legend(frameon=False)

plt.tight_layout()
fig.savefig('plot_configs_RbX18.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()
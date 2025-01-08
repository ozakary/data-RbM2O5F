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
data_1 = pd.read_csv("./step-2_OF_dist/concatenated_configs_NbX6_l.csv")
data_2 = pd.read_csv("./step-2_OF_dist/concatenated_configs_NbX6_h.csv")
data_3 = np.loadtxt("./Nb_anionic-environements_vf-all_publi.txt", skiprows=1, usecols=range(1, 7 + 1))

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
    p = np.arange(0, n + 1, 1)
    k = np.arange(n, -1, -1)
    Comb1 = []
    for i in range(len(p)):
        Comb = (math.factorial(n)) / (math.factorial(p[i]) * math.factorial(n - p[i]))
        Comb1.append(Comb)
    Proba = Comb1 * ((5 / 6) ** k) * ((1 / 6) ** p)
    return Proba * 100

# Set up parameters for the bar plot
n_groups = len(Prob_th_1)  # Adjust to the number of groups

index = np.arange(n_groups)

bar_width = 0.2
opacity = 0.25

bar_labelsNb = ['0', '1', '2', '3', '4', '5', '6']

fig, ax = plt.subplots(figsize=(4.5, 5.5))

# Plot the first probability with a starting point of 0
bar_plot_1 = ax.bar(index - bar_width, np.array(Prob_th_1) / 100, bar_width, color='#264653', alpha=1, bottom=0, label=r'$N_{select}\{E_{Ewald}^{(\searrow)}\}$')
bar_plot_2 = ax.bar(index, np.array(Prob_th_2) / 100, bar_width, color='#2A9D8F', alpha=1, bottom=0, label=r'$N_{select}\{E_{Ewald}^{(\nearrow)}\}$')
bar_plot_3 = ax.bar(index + bar_width, Proba_conf(6) / 100, bar_width, color='#E76F51', alpha=1, label='Formula')
bar_plot_4 = ax.bar(index + 2 * bar_width, np.array(Prob_th_3) / 100, bar_width, color='#F3B6A5', alpha=1, bottom=0, label=r'Selected')

ax.set_ylim(0, 1)
ax.set_xticks(index + bar_width * 0.5)
ax.set_xticklabels(bar_labelsNb)
ax.set_xlabel(r'$x$ in $[NbO_{6-x}F_{x}]^{n-}$', fontsize=18)
ax.set_ylabel(r'$P(x)$', fontsize=18)

plt.legend(frameon=False)

plt.tight_layout()
fig.savefig('plot_configs_NbX6.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()

print(np.array(Prob_th_2))

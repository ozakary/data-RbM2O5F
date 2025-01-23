#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

data_file = np.loadtxt("./figure_8-b_data.txt", skiprows=1)
labels = ['$f$ {$\delta_{iso}$ ; $^{19}F$}', '$f$ {$\delta_{CSA}$ ; $^{19}F$}',
          '$f$ {$C_Q$ ; $^{87}Rb$}', '$f$ {$\eta_Q$ ; $^{87}Rb$}', '$f$ {$\delta_{iso}$ ; $^{87}Rb$}']
colors = ['#E76F51', '#2A9D8F']
gr_labels = [r'unit cell', r'2$\times$2$\times$2 supercell']
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

data_file_2 = np.column_stack([data_file, data_file[:, 1]])
angles += angles[:1]

graph_y = [data_file_2[0, 1:], data_file_2[1, 1:]]

fig, axis = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
for i in  range(len(colors)):
    axis.plot(angles, graph_y[i], color=colors[i], linewidth=1, label=gr_labels[i])
    axis.scatter(angles, graph_y[i], s=15, color=colors[i], zorder=10)
    axis.fill(angles, graph_y[i], color=colors[i], alpha=0.05)
    axis.set_theta_offset(np.pi / 2)
    axis.set_theta_direction(-1)
    axis.set_thetagrids(np.degrees(angles[:-1]), labels)
for label, angle in zip(axis.get_xticklabels(), angles):
    if angle in (0, np.pi):
        label.set_horizontalalignment('center')
    elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')

y_tick_labels = ['0%', '20%', '40%', '60%', '80%', '100%'] 

axis.set_ylim(0, 100)
axis.set_yticks([0, 20, 40, 60, 80, 100])
axis.set_yticklabels(y_tick_labels)

ind = y_tick_labels.index('0%')

gridlines = axis.yaxis.get_gridlines()
gridlines[ind].set_linewidth(1)

axis.set_rlabel_position(180/num_vars)
axis.tick_params(axis='y')
axis.legend(bbox_to_anchor=(1.45, 1.4), frameon=False)


fig.savefig('RbTa2O5F_radars.svg', format='svg', dpi=300, bbox_inches='tight')
plt.show()

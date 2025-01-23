#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as mpatches

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

# Load the data and extract only the "energy (eV)" column
data_1 = pd.read_csv("./figure_5_data-1.csv")
data_2 = pd.read_csv("./figure_5_data-2.csv")

# Combine the energy columns from both datasets into one Series
energies = pd.concat([data_1["energy (eV)"], data_2["energy (eV)"]])

# Define a threshold for low and high energy coloring
threshold = energies.median()  # You can adjust this to a specific value if desired

# Define bins
bins = np.linspace(-3120, -3060, 250)  # 250 bins for fine-grained histogram

# Plot histogram with custom colors for bins
fig, ax = plt.subplots(figsize=(6, 4))

# Compute histogram data without plotting to get counts and bin edges
counts, bin_edges = np.histogram(energies, bins=bins)

# Create color array for bins
colors = []
for edge in bin_edges[:-1]:  # Exclude last edge for color assignment
    if edge < threshold:
        colors.append('#2A9D8F')  # Color for low energies
    else:
        colors.append('#F3B6A5')  # Color for high energies

# Plot histogram with specified bin colors
ax.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), color=colors, align="edge")

# Create legend items for low and high energies
low_energy_patch = mpatches.Patch(color='#2A9D8F', label=r'$N_{select}$ {$E_{Ewald}^{(\searrow)}$} = 5$\times10^{4}$')
high_energy_patch = mpatches.Patch(color='#F3B6A5', label=r'$N_{select}$ {$E_{Ewald}^{(\nearrow)}$} = 5$\times10^{4}$')

# Add legend to the plot
ax.legend(handles=[low_energy_patch, high_energy_patch], frameon=False, fontsize=14)

# Set labels and title
ax.set_xlabel(r'$E_{Ewald}$ / $eV$')
ax.set_ylabel(r'Structure count')

ax.set_xlim(-3120, -3060)
ax.set_ylim(0, 20000)


# Show plot
plt.tight_layout()
fig.savefig('plot_ewald_dist.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()

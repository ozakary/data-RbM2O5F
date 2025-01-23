#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker # changing the format of the 'z' axis ticks from 0.0001 to 1e-04, lines 7-9 and 27
from scipy.interpolate import griddata

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

# Import the figure_formatting module
import figure_formatting as ff

# Set up figure formatting using the function from the module
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

def generate_smooth_surface(input_file, elevation=25, azimuth=-125):
    # Read the input file into a numpy array
    data = np.genfromtxt(input_file, delimiter='\t', skip_header=1)

    # Extract columns
    cq = data[:, 1]
    nq = data[:, 2]
    mult = data[:, 3]

    # Define the range for CQ and nQ
    cq_range = np.arange(0, 6 + 0.1, 0.1)
    nq_range = np.arange(0, 1 + 0.1, 0.1)

    # Create a meshgrid from the ranges
    cq_grid, nq_grid = np.meshgrid(cq_range, nq_range)

    # Interpolate Multiplicity values
    mult_grid = griddata((cq, nq), mult, (cq_grid, nq_grid), method='linear', fill_value=0)

    # Create a 3D plot
    fig = plt.figure(1, figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    fig.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.2)

    # Plot the smooth surface
    ax.plot_surface(cq_grid, nq_grid, mult_grid, cmap='rainbow', rstride=1, cstride=1, linewidth=0, antialiased=True)

    # Set axis labels
#    ax.set_title('$^{87}$Rb $-$ RbNb$_2$O$_5$F (Without Mod. 6, 7 & 9)', fontname = 'Times New Roman', fontsize = 26, y = 1)
    ax.set_xlabel('C$_Q$ / MHz', fontsize = 20, labelpad = 20)
    ax.set_ylabel('η$_Q$', fontsize = 20, labelpad = 20)
    ax.set_zlabel('Multiplicity', fontsize = 20, labelpad = 20)

    # Set the viewing angle
    ax.view_init(elev=elevation, azim=azimuth)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: f'{y:.1f}'))
    
    ax.xaxis.set_tick_params(labelsize=16)
    ax.yaxis.set_tick_params(labelsize=16)
    ax.zaxis.set_tick_params(labelsize=16)
    ax.locator_params(axis='x', nbins=4)
    ax.set_zlim(0, 7)

    # Adding text in the 3D plot
    # Here, the text is added at the position (x, y, z) -> (3, 0.5, 0.3)
    ax.text(x=2, y=0.5, z=6, s=r'$^{87}$Rb $-$ RbNb$_{2}$O$_{5}$F', color='#161616', fontsize=18)

    # Show the plot
    fig.savefig('th_3d_87Rb_dist_RbNb2O5F.svg', format='svg', dpi=300, bbox_inches='tight', pad_inches=0.7)
    plt.show()
    print(np.min(cq))
    print(np.max(cq))
    print(np.min(nq))
    print(np.max(nq))


# Example usage
input_file = 'figure_7-d_data.txt'  # replace with your actual input file path
generate_smooth_surface(input_file, elevation=25, azimuth=-125)


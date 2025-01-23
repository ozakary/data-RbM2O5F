#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker # changing the format of the 'z' axis ticks from 0.0001 to 1e-04, lines 7-9 and 27

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

# Import the figure_formatting module
import figure_formatting as ff

# Set up figure formatting using the function from the module
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

# Function to calculate the probability distribution of CQ and etaQ
def P(C_Q, eta_Q):
    return ((C_Q**4 * eta_Q) / (np.sqrt(2 * np.pi) * (0.82598**5))) * ( 1 - 
        (eta_Q**2 / 9)) * np.exp(- (C_Q**2 / (2*(0.82598**2))) * (1 + (eta_Q**2 / 3))) # 995.42 (RbTa) and 825.98 (RbNb) 87Rb and 25783.45 (RbNb) 93Nb

# Variables:
C_Q = np.linspace(0, 6, 50) #(0, 3000, 50) and (0, 100000, 50) for 87Rb and 93Nb respectively
eta_Q = np.linspace(0, 1, 50)
X, Y = np.meshgrid(C_Q, eta_Q) # Putting CQ and etaQ in a 2D mesh
P_C_eta = P(X, Y) #Definning the z axis of the 3D graph

# Plotting the 3D graph
fig_one = plt.figure(1, figsize=(8, 8))

fig_one.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.2)

canvas = fig_one.add_subplot(111, projection='3d')
canvas.plot_surface(X, Y, P_C_eta, cmap='rainbow')
canvas.set_xlabel('C$_{Q}$ / MHz', fontsize = 20, labelpad=20) #labelpad is for shifting away the (x,y,z) labels from their ticks
canvas.set_ylabel('$\eta_{Q}$', fontsize = 20, labelpad=20)
canvas.set_zlabel('$P$ ×10$^{-1}$ / a.u.', fontsize = 20, labelpad=20)
canvas.view_init(25, -125) # To view the 3D graph from a specific angle

# Managing the graph ticks
canvas.zaxis.set_major_formatter(formatter)
canvas.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: f'{y:.1f}'))
canvas.xaxis.set_tick_params(labelsize=16)
canvas.yaxis.set_tick_params(labelsize=16)
canvas.zaxis.set_tick_params(labelsize=16)

# Handling colorbar ticks format and the scale factor x10^(-4)
canvas.zaxis.offsetText.set_visible(False) # To make the scale factor disappear 
canvas.locator_params(axis='x', nbins=4) # This line is verry useful, is to chose how much ticks to show in the targeted axis || nbins= 4 (RbNb) 87Rb
canvas.set_zlim(0, 0.5)

# Adding text in the 3D plot
# Here, the text is added at the position (x, y, z) -> (3, 0.5, 0.3)
canvas.text(x=2, y=0.5, z=0.45, s=r'$^{87}$Rb $-$ RbNb$_{2}$O$_{5}$F', color='#161616', fontsize=18)

def fmt(x, pos):
    a, b = '{:.1e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


fig_one.savefig('exp_3d_87Rb_dist_RbNb2O5F.svg', format='svg', dpi=300, bbox_inches='tight', pad_inches=0.7)
plt.show()

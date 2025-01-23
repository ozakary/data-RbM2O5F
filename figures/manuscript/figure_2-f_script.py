import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import MaxNLocator

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

# Fixed spectral ranges based on your input
F2_min_Hz = -1.2976e+05
F2_max_Hz = -3.2956e+05
F1_min_Hz = -58496.03
F1_max_Hz = -1.5771e+05

# Metadata parameters
N_F2 = 1024  # Number of data points along the F2 dimension
N_F1 = 128   # Number of data points along the F1 dimension

# Frequency parameters from the data file
Freq_F2 = 208.118 # Convert from MHz to Hz for F2
Freq_F1 = 98.278  # Convert from MHz to Hz for F1

# Calculate the frequency axes in Hz
F2_axis_Hz = np.linspace(F2_min_Hz, F2_max_Hz, N_F2)
F1_axis_Hz = np.linspace(F1_min_Hz, F1_max_Hz, N_F1)

# Conversion to ppm
F2_axis_ppm = F2_axis_Hz / Freq_F2
F1_axis_ppm = F1_axis_Hz / Freq_F1

# Load the data and reshape as before
file_path_1 = './figure_2-f_data-1.asc'  # Path to the uploaded file
file_path_2 = 'figure_2-f_data-2.asc'  # Path to the uploaded file

data_exp = np.loadtxt(file_path_1, skiprows=13)
data_fit = np.loadtxt(file_path_2, skiprows=13)

# Reshaping the data to form a 2D array (N_F1 x N_F2)
spectrum_2d_exp = data_exp.reshape(N_F1, N_F2)
spectrum_2d_fit = data_fit.reshape(N_F1, N_F2)

# Create figure and gridspec layout
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(3, 3, height_ratios=[1, 3, 1], width_ratios=[1, 3, 1])

# Create the main contour plot
ax_main = fig.add_subplot(gs[1, 1])

# Calculate contour levels based on specifications
max_value_exp = np.max(spectrum_2d_exp) * 1.45
min_value_exp = np.min(spectrum_2d_exp)
num_contours_exp = 16
num_contours_fit = 12

# Create the contour levels
contour_levels_exp = np.linspace(min_value_exp, max_value_exp, num_contours_exp)

# Adjust contouring for the fit data similarly
max_value_fit = np.max(spectrum_2d_fit) * 0.9 #2.45
min_value_fit = np.min(spectrum_2d_fit)
contour_levels_fit = np.linspace(min_value_fit, max_value_fit, num_contours_fit)

# Update the contour plot creation
contour_exp = ax_main.contour(F2_axis_ppm, F1_axis_ppm, spectrum_2d_exp, 
                              levels=contour_levels_exp, colors='#264653', linewidths=2.5)
contour_fit = ax_main.contour(F2_axis_ppm, F1_axis_ppm, spectrum_2d_fit, 
                              levels=contour_levels_fit, colors='red', linestyles='--')

# # Create the contour plot with increased number of contours
# contour_exp = ax_main.contour(F2_axis_ppm, F1_axis_ppm, spectrum_2d_exp, levels=contour_levels_fit, colors='#264653', linewidths=2.5) #
# contour_fit = ax_main.contour(F2_axis_ppm, F1_axis_ppm, spectrum_2d_fit, levels=contour_levels_fit, colors='red', linestyles='--') # 
ax_main.plot(F2_axis_ppm, F2_axis_ppm, color='#F3B6A5')

# Create dummy handles for the legend
exp_legend = plt.Line2D([0], [0], color='#264653', linewidth=2.5, label='Experimental')
fit_legend = plt.Line2D([0], [0], color='red', linestyle='--', label='Fitted')  # Dashed for fitted
line_legend = plt.Line2D([0], [0], color='#2A9D8F', label='Line 1')
delta_model_legend = plt.Line2D([0], [0], color='grey', label=r'$\Delta_{model}$')  # Dashed for fitted

# Adding the legend to the main plot
ax_main.legend(frameon=False, handles=[exp_legend, fit_legend, line_legend, delta_model_legend], loc='upper left')

ax_main.set_xlabel(r'$^{93}Nb$ $MAS$ / $ppm$')
ax_main.set_ylabel(r'$^{93}Nb$ $Isotropic$ / $ppm$')
ax_main.invert_xaxis()  # Invert x-axis to match chemical shift convention
ax_main.set_xlim(-800, -1400)
ax_main.set_ylim(-800, -1400)

# Set the number of ticks for the x-axis
ax_main.xaxis.set_major_locator(MaxNLocator(nbins=3))
ax_main.yaxis.set_major_locator(MaxNLocator(nbins=3))

# Projection on the top (x,z)
ax_top = fig.add_subplot(gs[0, 1], sharex=ax_main)
ax_top.plot(F2_axis_ppm, np.sum(spectrum_2d_exp, axis=0) + 2000000, color='#264653', linewidth=2.5)
ax_top.plot(F2_axis_ppm, np.sum(spectrum_2d_fit, axis=0) + 2050000, color='red', linestyle='--')
ax_top.plot(F2_axis_ppm, np.sum(spectrum_2d_fit, axis=0) + 1200000, color='#2A9D8F')
ax_top.plot(F2_axis_ppm, (np.sum(spectrum_2d_fit, axis=0) + 2050000 - np.sum(spectrum_2d_exp, axis=0) - 2000000) + 400000, color='grey')
ax_top.set_xlim(-800, -1400)
ax_top.set_ylim(0, 3500000)

# Temporarily disable shared x-axis before removing ticks and labels
ax_top.xaxis.set_visible(False)
ax_top.yaxis.set_visible(False)


# Projection on the right (y,z)
ax_right = fig.add_subplot(gs[1, 2], sharey=ax_main)
ax_right.plot(np.sum(spectrum_2d_exp, axis=1) + 30000000, F1_axis_ppm, color='#264653', linewidth=2.5)
ax_right.plot(np.sum(spectrum_2d_fit, axis=1) + 30000000, F1_axis_ppm, color='red', linestyle='--')
ax_right.plot(np.sum(spectrum_2d_fit, axis=1) + 22500000, F1_axis_ppm, color='#2A9D8F')
ax_right.plot((np.sum(spectrum_2d_fit, axis=1) + 30000000 - np.sum(spectrum_2d_exp, axis=1) - 30000000) + 15000000, F1_axis_ppm, color='grey')
ax_right.set_xlim(5000000, 45000000)
ax_right.set_ylim(-800, -1400)

# Temporarily disable shared x-axis before removing ticks and labels
ax_right.xaxis.set_visible(False)
ax_right.yaxis.set_visible(False)

#plt.tight_layout()
plt.savefig("figure_exp_vs_fit_spectra_with_projections.svg")  # Save the plot as a PDF
plt.show()

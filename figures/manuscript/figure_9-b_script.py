import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import seaborn as sns

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

# Function to plot the spectra
def plot_combined_and_experimental_spectrum(chunk_files, experimental_file, operating_frequency_mhz):
    combined_intensity = None
    combined_delta_iso = None

    # Combine simulated spectrum from all chunks
    for chunk_file in chunk_files:
        chunk_df = pd.read_csv(chunk_file)

        if combined_intensity is None:
            combined_intensity = chunk_df['Intensity']
            combined_delta_iso = chunk_df['Delta_ISO (ppm)']
        else:
            combined_intensity += chunk_df['Intensity']  # Sum the intensities

    # Read the experimental data, skipping the first two rows
    experimental_data = pd.read_csv(
        experimental_file,
        comment='#',  # Skip comment lines
        delim_whitespace=True,  # Use whitespace as delimiter
        header=None,  # No header in the file
        names=['Frequency (Hz)', 'Intensity_Exp', 'Intensity_Fit', 'Intensity_Cont-1', 'Intensity_Cont-2']  # Assign column names
    )

    # Convert Frequency from Hz to ppm
    experimental_data['Delta_ISO (ppm)'] = experimental_data['Frequency (Hz)'] / operating_frequency_mhz

    # Optionally scale the experimental intensity for better comparison
    experimental_data['Intensity_scaled'] = experimental_data['Intensity_Exp'] - 100 # Scale if necessary

    # Initialize a figure for plotting
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    # Plot the experimental spectrum
    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_scaled'] + 1000, 
        label='Experimental', 
        color='#264653'
    )

    # Plot the theoretical spectrum
    ax.plot(combined_delta_iso, combined_intensity*525 + 900, label='Theoretical', color='#2A9D8F', linestyle='dashed')

    # Plot settings
    ax.set_xlabel(r'$^{19}F$ $frequency$ / $ppm$')
    plt.gca().invert_xaxis()  # Invert x-axis to match chemical shift convention
    ax.set_xlim(50, -250)
    plt.legend(frameon=False)
    plt.tight_layout()

    #Add asterisks
    ax.text(
    -45, 1200,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    -180, 1200,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    18, 900,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    -243, 900,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    # Add the inset plot
    ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper left", borderpad=1)

#    # Add the inset plot manually with custom coordinates
#    inset_position = [0.15, 0.6, 0.3, 0.3]  # [left, bottom, width, height] in figure coordinates
#    ax_inset = fig.add_axes(inset_position)

    ax_inset.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_scaled'] + 2000, 
        color='#264653'
    )
    ax_inset.plot(combined_delta_iso, combined_intensity*525 + 2000, color='#2A9D8F', linestyle='dashed')

    # Zoomed region settings
    ax_inset.set_xlabel(r'$^{19}F$ $frequency$ / $ppm$')
    ax_inset.set_xlim(-140, -60)
#    ax_inset.set_ylim(0, max(combined_intensity*10)-2000)  # Adjust the y-limits if needed
    ax_inset.invert_xaxis()  # Invert x-axis in the inset as well
#    ax_inset.set_xticks([])  # Remove x-axis ticks in the inset
#    ax_inset.set_yticks([])  # Remove y-axis ticks in the inset

    # Save and show the figure
    plt.savefig("19F_th_vs_exp_RbTa2O5F.pdf")  # Save the plot as a PDF
    plt.show()

# Main execution
if __name__ == "__main__":
    experimental_file = 'figure_9-b_data-1.asc'
    operating_frequency_mhz = 800.072  # Operating frequency in MHz

    # Dynamically collect all chunk files matching the pattern
    chunk_files = glob.glob("./simulated_spectrum_chunk_*.csv")

    plot_combined_and_experimental_spectrum(chunk_files, experimental_file, operating_frequency_mhz)

    print("Simulation, comparison, and plotting completed.")

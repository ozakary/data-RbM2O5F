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
    experimental_data['Intensity_scaled'] = experimental_data['Intensity_Exp']  # Scale if necessary

    # Initialize a figure for plotting
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # Plot the experimental spectrum
    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_scaled'] / 54, 
        label='Experimental', 
        color='#264653'
    )

    # Plot the theoretical spectrum
    ax.plot(combined_delta_iso, combined_intensity*0.43e4 + 1500, label='Theoretical', color='#2A9D8F', linestyle='dashed')

    # Plot settings
    ax.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    plt.gca().invert_xaxis()  # Invert x-axis to match chemical shift convention
    ax.set_xlim(2650, -2650)
    plt.legend(frameon=False, bbox_to_anchor=(0.85, 0.43), loc="center")
    plt.tight_layout()

    # Add the inset plot
    ax_inset_1 = inset_axes(ax, width="40%", height="22%", loc="upper left", borderpad=1)

    ax_inset_1.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_scaled'] / 54 + 0.5e4, 
        color='#264653'
    )
    ax_inset_1.plot(combined_delta_iso, combined_intensity*0.43e4 + 0.5e4, color='#2A9D8F', linestyle='dashed')

    # Zoomed region settings
    ax_inset_1.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    ax_inset_1.set_xlim(-120, -40)
    ax_inset_1.set_ylim(0, 3.4e4)  # Adjust the y-limits if needed
    ax_inset_1.invert_xaxis()  # Invert x-axis in the inset as well

    # Add the inset 2 plot
    ax_inset_2 = inset_axes(ax, width="25%", height="22%", loc="upper right", borderpad=1)

    ax_inset_2.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Exp'] / 54 + 250, 
        linewidth=2.5,
        color='#264653'
    )
    ax_inset_2.plot(combined_delta_iso, combined_intensity*0.43e4 + 250, color='#2A9D8F', linestyle='dashed')

    # Zoomed region settings
    ax_inset_2.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    ax_inset_2.set_xlim(-250, -150)
    ax_inset_2.set_ylim(0, 1700)  # Adjust the y-limits if needed
    ax_inset_2.invert_xaxis()  # Invert x-axis in the inset as well

    # Save and show the figure
    plt.savefig("simulated_vs_experimental_spectrum_with_inset.svg")  # Save the plot as a PDF
    plt.show()

# Main execution
if __name__ == "__main__":
    experimental_file = 'exp_vs_fit_spec_and_model_all_lines.asc'
    operating_frequency_mhz = 278.221  # Operating frequency in MHz

    # Dynamically collect all chunk files matching the pattern
    chunk_files = glob.glob("./simulated_spectrum_chunk_*.csv")

    plot_combined_and_experimental_spectrum(chunk_files, experimental_file, operating_frequency_mhz)

    print("Simulation, comparison, and plotting completed.")

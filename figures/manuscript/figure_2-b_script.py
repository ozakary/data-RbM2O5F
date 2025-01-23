import pandas as pd
import matplotlib.pyplot as plt

# Import the figure_formatting module (optional, remove if not needed)
import figure_formatting as ff

# Set up figure formatting using the function from the module (optional)
ff.set_rcParams(ff.master_formatting)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from typing import Optional

#colors = ['#264653', '#2A9D8F', '#E9C46A', '#E76F51', '#F3B6A5']

# Function to read and plot the experimental spectrum
def plot_experimental_spectrum(file_path, operating_frequency_mhz):
    # Read the experimental data, skipping the first two rows
    experimental_data = pd.read_csv(
        file_path,
        comment='#',  # Skip comment lines
        delim_whitespace=True,  # Use whitespace as delimiter
        header=None,  # No header in the file
        names=['Frequency (Hz)', 'Intensity_Exp', 'Intensity_Fit', 'Intensity_Cont-1', 'Intensity_Cont-2']  # Assign column names
    )

    # Convert Frequency from Hz to ppm
    experimental_data['Delta_ISO (ppm)'] = experimental_data['Frequency (Hz)'] / operating_frequency_mhz

    # Initialize a figure for plotting
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # Plot the experimental spectrum
    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Exp'], 
        label='Experimental',
        linewidth=2.5,
        color='#264653'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Fit'], 
        label='Fitted', 
        color='red',#'#2A9D8F',
        linestyle='dashed'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Cont-2'] - 140000, 
        label='Line 1', 
        color='#2A9D8F'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Cont-1'] - 280000, 
        label=r'STSS ($n = 0$)', 
        color='#E76F51'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        (experimental_data['Intensity_Exp'] - experimental_data['Intensity_Fit']) - 420000, 
        label=r'$\Delta_{model}$', 
        color='grey'
    )

    # Plot settings
    # Plot settings
    ax.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    plt.gca().invert_xaxis()  # Invert x-axis to match chemical shift convention
    ax.set_xlim(2650, -2650)
    plt.legend(frameon=False, bbox_to_anchor=(0.85, 0.43), loc="center")

    # Add the inset 1 plot
    ax_inset_1 = inset_axes(ax, width="40%", height="22%", loc="upper left", borderpad=1)

    ax_inset_1.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Exp'], 
        linewidth=2.5,
        color='#264653'
    )

    ax_inset_1.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Fit'], 
        color='red',#'#2A9D8F',
        linestyle='dashed'
    )

    # Zoomed region settings
    ax_inset_1.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    ax_inset_1.set_xlim(-120, -40)
#    ax_inset.set_ylim(0, max(combined_intensity*50))  # Adjust the y-limits if needed
    ax_inset_1.invert_xaxis()  # Invert x-axis in the inset as well


    # Add the inset 2 plot
    ax_inset_2 = inset_axes(ax, width="40%", height="22%", loc="upper right", borderpad=1)

    ax_inset_2.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Exp'], 
        linewidth=2.5,
        color='#264653'
    )

    ax_inset_2.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Fit'], 
        color='red',#'#2A9D8F',
        linestyle='dashed'
    )

    # Zoomed region settings
    ax_inset_2.set_xlabel(r'$^{87}Rb$ $frequency$ / $ppm$')
    ax_inset_2.set_xlim(-450, -150)
    ax_inset_2.set_ylim(0, 65000)  # Adjust the y-limits if needed
    ax_inset_2.invert_xaxis()  # Invert x-axis in the inset as well


    plt.tight_layout()
    plt.savefig("figure_exp_vs_fit_spectra.pdf")  # Save the plot as a PDF
    plt.show()  # Display the plot



# Main execution
if __name__ == "__main__":
    experimental_file = 'figure_2-b_data.asc'
    operating_frequency_mhz = 278.221  # Operating frequency in MHz
    plot_experimental_spectrum(experimental_file, operating_frequency_mhz)
    print("Experimental spectrum plotted successfully.")


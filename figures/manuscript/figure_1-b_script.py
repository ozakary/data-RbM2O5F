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
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

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
        experimental_data['Intensity_Cont-1'] - 1000, 
        label='Line 1', 
        color='#2A9D8F'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Cont-2'] - 2000, 
        label='Line 2', 
        color='#E76F51'
    )

    ax.plot(
        experimental_data['Delta_ISO (ppm)'], 
        (experimental_data['Intensity_Exp'] - experimental_data['Intensity_Fit']) - 3000, 
        label=r'$\Delta_{model}$', 
        color='grey'
    )

    #Add asterisks
    ax.text(
    -45, 200,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    -180, 200,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    18, 10,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    ax.text(
    -243, 10,  # x, y coordinates for the text
    '*',                           # Text to display
    fontsize=22,                               # Font size of the text
    color='#264653',                             # Text color
    ha='center',                               # Horizontal alignment (center, left, right)
    va='bottom'                                # Vertical alignment (top, center, bottom)
    )

    # Plot settings
    # Plot settings
    ax.set_xlabel(r'$^{19}F$ $frequency$ / $ppm$')
    plt.gca().invert_xaxis()  # Invert x-axis to match chemical shift convention
    ax.set_xlim(50, -250)
    plt.legend(frameon=False)

    # Add the inset plot
    ax_inset = inset_axes(ax, width="40%", height="30%", loc="upper left", borderpad=1)

    ax_inset.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Exp'], 
        linewidth=2.5,
        color='#264653'
    )

    ax_inset.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity_Fit'], 
        color='red',#'#2A9D8F',
        linestyle='dashed'
    )

    # Zoomed region settings
    ax_inset.set_xlabel(r'$^{19}F$ $frequency$ / $ppm$')
    ax_inset.set_xlim(-140, -60)
#    ax_inset.set_ylim(0, max(combined_intensity*50))  # Adjust the y-limits if needed
    ax_inset.invert_xaxis()  # Invert x-axis in the inset as well



    plt.tight_layout()
    plt.savefig("figure_exp_vs_fit_spectra.pdf")  # Save the plot as a PDF
    plt.show()  # Display the plot



# Main execution
if __name__ == "__main__":
    experimental_file = 'figure_1-b_data.asc'
    operating_frequency_mhz = 800.072  # Operating frequency in MHz
    plot_experimental_spectrum(experimental_file, operating_frequency_mhz)
    print("Experimental spectrum plotted successfully.")


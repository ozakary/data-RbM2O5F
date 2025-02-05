# Import necessary libraries from mrsimulator and other required packages

from mrsimulator import Simulator, SpinSystem, Site
from mrsimulator import signal_processor as sp
from mrsimulator.method.lib import BlochDecayCTSpectrum
from mrsimulator.spin_system.tensors import SymmetricTensor
from mrsimulator.method import SpectralDimension

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tempfile
import os

# Function to read the data file and create Site objects
def read_sites_from_file(filename):
    sites = []
    with open(filename, 'r') as file:
        for line in file:
            # Skip empty lines or comment lines if needed
            if line.strip() and not line.startswith('#'):
                # Split the line into components
                data = line.split()
                
                # Assuming the relevant data columns based on your description:
                delta_iso = float(data[2])  # 3rd column
                delta_csa = float(data[3]) * -3 # 4th column
                eta_csa = float(data[4])  # 5th column
                C_Q = float(data[5]) * 1e6  # 6th column
                eta_Q = float(data[6])  # 7th column
                
                # Create a Site object for each row
                site = Site(
                    isotope="87Rb",
                    isotropic_chemical_shift=delta_iso,  # in ppm
                    shielding_symmetric=SymmetricTensor(
                        zeta=delta_csa,  # delta_csa in ppm
                        eta=eta_csa,     # eta_csa
                    ),                    
                    quadrupolar=SymmetricTensor(
                        Cq=C_Q,  # delta_csa in ppm
                        eta=eta_Q,     # eta_csa
                    ),
                )
                sites.append(site)
    return sites

# Function to simulate and save chunks of the spectrum
def simulate_and_save_chunks(input_filename, chunk_size=4):
    all_files = []
    
    # Read the input file and process in chunks
    all_sites = read_sites_from_file(input_filename)
    num_chunks = len(all_sites) // chunk_size + (len(all_sites) % chunk_size > 0)

    for i in range(num_chunks):
        print(f"Processing chunk {i + 1} of {num_chunks}...")  # Progress statement
        chunk_sites = all_sites[i * chunk_size:(i + 1) * chunk_size]

        # Set abundance to 1 for each site
        abundance = [100] * len(chunk_sites)
        spin_systems = [SpinSystem(sites=[s], abundance=a) for s, a in zip(chunk_sites, abundance)]

        # Create the BlochDecaySpectrum method object
        method = BlochDecayCTSpectrum(
            channels=["87Rb"],
            magnetic_flux_density=20,  # in T
            rotor_angle=54.735 * 3.14159 / 180,  # in rad (magic angle)
            rotor_frequency=30e3,  # in Hz (10 kHz as specified)
            spectral_dimensions=[
                SpectralDimension(
                    count=1000,
                    spectral_width=1.45e6,  # in Hz
                    label=r"$^{87}$Rb resonances",
                )
            ],
        )

        # Create a Simulator object with the spin system and method
        sim = Simulator()
        sim.spin_systems = spin_systems
        sim.methods = [method]
        sim.run()

        # Create the SignalProcessor object for line broadening
        processor = sp.SignalProcessor(
            operations=[
                sp.IFFT(),
                sp.apodization.Exponential(FWHM="10 Hz"),  # Line broadening
                sp.apodization.Gaussian(FWHM="2000 Hz"),
                sp.FFT(),
            ]
        )

        # Apply the processor to the simulation dataset
        processed_simulation = processor.apply_operations(dataset=sim.methods[0].simulation)

        # Save the representation of processed_simulation.real to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            # Writing the string representation to the file
            temp_file.write(str(processed_simulation.real))
            temp_file_path = temp_file.name  # Store the path of the temporary file

        # Read from the temporary file to extract Intensity and delta_iso
        with open(temp_file_path, 'r') as file:
            data = file.read()

        # Extract intensity values
        start_intensity = data.find("DependentVariable(") + len("DependentVariable(\n[[")
        end_intensity = data.find("]], quantity_type=scalar")
        intensity_str = data[start_intensity:end_intensity].strip()

        # Convert the string of intensity values to a numpy array
        intensity_values = np.fromstring(intensity_str, sep=' ')

        # Extract delta_iso values
        start_delta_iso = data.find("LinearDimension([") + len("LinearDimension([")
        end_delta_iso = data.find("] ppm)")
        delta_iso_str = data[start_delta_iso:end_delta_iso].strip()

        # Convert the string of delta_iso values to a numpy array
        delta_iso_values = np.fromstring(delta_iso_str, sep=' ')

        # Create a DataFrame
        data_df = pd.DataFrame({
            'Delta_ISO (ppm)': delta_iso_values,
            'Intensity': intensity_values
        })

        # Save to a CSV file
        output_filename = f'simulated_spectrum_chunk_{i + 1}.csv'
        data_df.to_csv(output_filename, index=False)
        all_files.append(output_filename)
    
    print("All chunks processed successfully.")
    return all_files

# Function to plot the combined spectrum from all chunks
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
        names=['Frequency (Hz)', 'Intensity', 'Model', 'Line1', 'Line2']  # Assign column names
    )

    # Convert Frequency from Hz to ppm
    experimental_data['Delta_ISO (ppm)'] = experimental_data['Frequency (Hz)'] / operating_frequency_mhz
    experimental_data['Intensity x 200'] = experimental_data['Intensity'] * 80

    # Plot the combined simulated spectrum
    plt.figure(figsize=(5, 3))
    plt.plot(combined_delta_iso, combined_intensity*5.9e5, label='Th.', color='blue')
    
    # Plot the experimental spectrum
    plt.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity x 200'], 
        label='Exp.', 
        color='red'
    )
    
    # Plot settings
    plt.title("MAS NMR Spectra of $^{87}Rb$")
    plt.xlabel("Chemical Shift (ppm)")
    plt.ylabel("Intensity")
    plt.xlim(2500, -2500)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main execution
input_filename = 'models_2-3-4-8-9_Rb.gipaw' #'data_test.gipaw'
experimental_file = 'exp_vs_fit_spec_and_model_all_lines.asc'
operating_frequency_mhz = 278.221  # Operating frequency in MHz

chunk_files = simulate_and_save_chunks(input_filename, chunk_size=4)
plot_combined_and_experimental_spectrum(chunk_files, experimental_file, operating_frequency_mhz)

print("Simulation, comparison, and plotting completed.")


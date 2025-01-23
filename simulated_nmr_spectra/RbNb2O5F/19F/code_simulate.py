# Import necessary libraries from mrsimulator and other required packages
from mrsimulator import Site, SpinSystem, Simulator
from mrsimulator.method.lib import BlochDecaySpectrum
from mrsimulator.method import SpectralDimension
from mrsimulator import signal_processor as sp
from mrsimulator.spin_system.tensors import SymmetricTensor
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
                delta_csa = float(data[3])   # 4th column
                eta_csa = float(data[4])     # 5th column
                
                # Create a Site object for each row
                site = Site(
                    isotope="19F",
                    isotropic_chemical_shift=delta_iso,  # in ppm
                    shielding_symmetric=SymmetricTensor(
                        zeta=delta_csa,  # delta_csa in ppm
                        eta=eta_csa,     # eta_csa
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

        # Create the SpinSystem object with the dynamically created sites
        spin_system = SpinSystem(sites=chunk_sites)

        # Create the BlochDecaySpectrum method object
        method = BlochDecaySpectrum(
            channels=["19F"],
            magnetic_flux_density=20,  # in T
            rotor_angle=54.735 * 3.14159 / 180,  # in rad (magic angle)
            rotor_frequency=46e3,  # in Hz (10 kHz as specified)
            spectral_dimensions=[
                SpectralDimension(
                    count=512,
                    spectral_width=800e3,  # in Hz
                    reference_offset=0,  # Set to 0 for a centered spectrum
                    label=r"$^{19}$F resonances",
                )
            ],
        )

        # Create a Simulator object with the spin system and method
        sim = Simulator(spin_systems=[spin_system], methods=[method])
        sim.run()

        # Create the SignalProcessor object for line broadening
        processor = sp.SignalProcessor(
            operations=[
                sp.IFFT(),
                sp.apodization.Gaussian(FWHM='8000 Hz', dim_index=0, dv_index=0),  # Line broadening
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
    experimental_data['Intensity x 200'] = experimental_data['Intensity']*200

    # Plot the combined simulated spectrum
    plt.figure(figsize=(5, 3))
    plt.plot(combined_delta_iso, combined_intensity, label='Simulated Spectrum', color='blue')
    
    # Plot the experimental spectrum
    plt.plot(
        experimental_data['Delta_ISO (ppm)'], 
        experimental_data['Intensity x 200'], 
        label='Experimental Spectrum', 
        color='red', 
        linestyle='dashed'
    )

    # Plot settings
    plt.title("Simulated vs Experimental MAS NMR Spectrum of $^{19}F$")
    plt.xlabel("Chemical Shift (ppm)")
    plt.ylabel("Intensity")
#    plt.xlim(100, -300)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.tight_layout()
    plt.savefig("simulated_vs_experimental_spectrum.pdf")
    plt.show()

# Main execution
input_filename = 'models_2-3-4-8-9_F.gipaw'
experimental_file = 'exp_vs_fit_vf_spec_and_model_all_lines.asc'
operating_frequency_mhz = 800.072  # Operating frequency in MHz

chunk_files = simulate_and_save_chunks(input_filename, chunk_size=4)
plot_combined_and_experimental_spectrum(chunk_files, experimental_file, operating_frequency_mhz)

print("Simulation, comparison, and plotting completed.")


from ase.io import read
import numpy as np
from collections import Counter
import csv
import os
import time

# Set the cutoff distance for Rb-X bonding
cutoff_distance = 4.2

# Base path to the directory where the .cif files and the input text file are located
base_directory = './step-2_OF_dist/Rb_config-5/'

# Path to the file containing the structure paths and energies
input_file = os.path.join(base_directory, '2nd_step_coulomb_energy_h.txt')
output_file = os.path.join(base_directory, 'RbX18_step-2_OF_dist_Rb_config-5_summary_h.csv')

# Read the input file
with open(input_file, 'r') as f:
    structures = [line.split() for line in f]

# Initialize the output data list
output_data = []

# Define the RbX18 cage configurations of interest
configurations_of_interest = [f'RbO{18 - x}F{x}' for x in range(19)]  # RbO18, RbO17F1, ..., RbF18

# Start the timer
start_time = time.time()

# Process each structure in the input file
total_structures = len(structures)
for index, structure_info in enumerate(structures):
    # Prepend './' to the structure path
    structure_path = './' + structure_info[0]
    energy = float(structure_info[1])

    # Check if the file exists
    if os.path.isfile(structure_path):
        print(f"Processing file: {structure_path} with energy: {energy} eV")
        
        # Load the structure from the .cif file
        structure = read(structure_path)

        # Select the Rb atoms from the original unit cell
        rb_atoms = [atom for atom in structure if atom.symbol == 'Rb']
        x_atoms = [atom for atom in structure if atom.symbol in ('O', 'F')]

        # Initialize a list to hold the cage configurations
        cage_configs = []

        # For each Rb atom, calculate distances to nearby O and F atoms and classify the configuration
        for rb_atom in rb_atoms:
            # Find neighboring atoms within the cutoff distance considering PBC
            neighbors = [x for x in x_atoms if structure.get_distance(rb_atom.index, x.index, mic=True) <= cutoff_distance]

            # Check if we have exactly 18 neighbors
            if len(neighbors) != 18:
                print(f"Warning: Rb atom at index {rb_atom.index} in {structure_path} has {len(neighbors)} neighbors (expected 18).")
                continue  # Skip to the next Rb atom if the count is not 18

            # Count the types of neighbors around this Rb atom
            neighbor_elements = [atom.symbol for atom in neighbors]
            config_count = Counter(neighbor_elements)

            # Classify based on the counts of 'O' and 'F' neighbors
            o_count = config_count.get('O', 0)
            f_count = config_count.get('F', 0)
            config = f'RbO{o_count}F{f_count}'

            # Store the configuration
            cage_configs.append(config)

        # Count each unique cage configuration for this structure
        config_summary = Counter(cage_configs)

        # Debug print the counted configurations for verification
        print(f"Configuration summary for {structure_path}: {config_summary}")

        # Prepare data row for this structure
        row = {
            'structure': structure_path,
            'energy (eV)': energy,
            **{config: config_summary.get(config, 0) for config in configurations_of_interest}
        }

        # Append the row to output data
        output_data.append(row)

    else:
        print(f"File not found: {structure_path}")

    # Calculate and print the progress
    progress_percentage = (index + 1) / total_structures * 100
    print(f"Progress: {progress_percentage:.2f}% ({index + 1}/{total_structures}) structures processed.")

# Write the results to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    # Use only the configurations of interest for the header
    fieldnames = ['structure', 'energy (eV)'] + configurations_of_interest
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in output_data:
        writer.writerow(data)

# Stop the timer
end_time = time.time()
execution_time = end_time - start_time
print(f"Results saved to {output_file}")
print(f"Total execution time: {execution_time:.2f} seconds.")


from ase.io import read
import numpy as np
from collections import Counter
import csv
import os
import time

# Set the cutoff distance for Nb-X bonding
cutoff_distance = 2.0

# Base path to the directory where the .cif files and the input text file are located
base_directory = './step-2_OF_dist/Rb_config-5/'

# Path to the file containing the structure paths and energies
input_file = os.path.join(base_directory, '2nd_step_coulomb_energy_h.txt')
output_file = os.path.join(base_directory, 'oct_step-2_OF_dist_Rb_config-5_summary_h.csv')

# Read the input file
with open(input_file, 'r') as f:
    structures = [line.split() for line in f]

# Initialize the output data list
output_data = []

# Define the octahedral configurations of interest
configurations_of_interest = ['NbO6F0', 'NbO5F1', 'NbO4F2', 'NbO3F3', 'NbO2F4', 'NbO1F5', 'NbO0F6']

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

        # Expand the structure to ensure full atomic environments are captured
        expanded_structure = structure * (2, 2, 2)  # Create a 2x2x2 supercell

        # Filter atoms by their types in the expanded structure
        nb_atoms = [atom for atom in expanded_structure if atom.symbol == 'Nb']
        x_atoms = [atom for atom in expanded_structure if atom.symbol in ('O', 'F')]

        # Initialize a list to hold the octahedral configurations and track unique Nb atoms
        octahedral_configs = []
        unique_nb_positions = set()

        # For each Nb atom, calculate distances to nearby O and F atoms and classify the configuration
        for nb_atom in nb_atoms:
            # Identify Nb atoms within the bounds of the original unit cell
            if tuple(np.round(nb_atom.position % structure.cell.diagonal(), decimals=3)) in unique_nb_positions:
                continue  # Skip already counted Nb atoms within the original cell

            # Add this Nb atom position to the set of unique positions
            unique_nb_positions.add(tuple(np.round(nb_atom.position % structure.cell.diagonal(), decimals=3)))

            # Find neighboring atoms within the cutoff distance
            neighbors = [x for x in x_atoms if expanded_structure.get_distance(nb_atom.index, x.index) <= cutoff_distance]

            # Ensure exactly 6 neighbors are identified for octahedral coordination
            if len(neighbors) != 6:
                continue

            # Count the types of neighbors around this Nb atom
            neighbor_elements = [atom.symbol for atom in neighbors]
            config_count = Counter(neighbor_elements)

            # Classify based on the counts of 'O' and 'F' neighbors
            o_count = config_count.get('O', 0)
            f_count = config_count.get('F', 0)
            config = f'NbO{o_count}F{f_count}'

            # Store the configuration
            octahedral_configs.append(config)

        # Count each unique octahedral configuration for this structure
        config_summary = Counter(octahedral_configs)

        # Debug print the counted configurations for verification
        print(f"Configuration summary for {structure_path}: {config_summary}")

        # Prepare data row for this structure
        row = {
            'structure': structure_path,
            'energy (eV)': energy,
            'NbO6F0': config_summary.get('NbO6F0', 0),
            'NbO5F1': config_summary.get('NbO5F1', 0),
            'NbO4F2': config_summary.get('NbO4F2', 0),
            'NbO3F3': config_summary.get('NbO3F3', 0),
            'NbO2F4': config_summary.get('NbO2F4', 0),
            'NbO1F5': config_summary.get('NbO1F5', 0),
            'NbO0F6': config_summary.get('NbO0F6', 0)
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


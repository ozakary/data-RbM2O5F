import pandas as pd

# List of file paths
file_paths = [
    './step-2_OF_dist/Rb_config-1/oct_step-2_OF_dist_Rb_config-1_summary_h.csv',
    './step-2_OF_dist/Rb_config-2/oct_step-2_OF_dist_Rb_config-2_summary_h.csv',
    './step-2_OF_dist/Rb_config-3/oct_step-2_OF_dist_Rb_config-3_summary_h.csv',
    './step-2_OF_dist/Rb_config-4/oct_step-2_OF_dist_Rb_config-4_summary_h.csv',
    './step-2_OF_dist/Rb_config-5/oct_step-2_OF_dist_Rb_config-5_summary_h.csv'
]

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through each file path
for i, file_path in enumerate(file_paths):
    if i == 0:
        # Read the first file with the header
        df = pd.read_csv(file_path)
    else:
        # Read subsequent files without the header
        df = pd.read_csv(file_path, header=0)  # Use header=0 to read the second row as header

    # Append the DataFrame to the list
    dataframes.append(df)

# Concatenate all DataFrames vertically
concatenated_df = pd.concat(dataframes, ignore_index=True)

# Save the concatenated DataFrame to a new CSV file
concatenated_df.to_csv('./step-2_OF_dist/concatenated_configs_NbX6_h.csv', index=False)

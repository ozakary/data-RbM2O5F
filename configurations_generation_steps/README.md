# Computational Protocol for RbNb<sub>2</sub>O<sub>5</sub>F Structural Configurations

**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This repository contains the computational protocol used to generate and analyze structural configurations of RbNb<sub>2</sub>O<sub>5</sub>F pyrochlore-type oxyfluorides, as described in the manuscript **"Revealed Preferential Anion Ordering in Disordered RbNb<sub>2</sub>O<sub>5</sub>F (M = Nb, Ta) Pyrochlore-Type Oxyfluorides"**.

## Prerequisites

### Required Software
- Supercell program ([Download](https://orex.github.io/supercell/))
- Python 3.x
- Required Python packages:
  - matplotlib
  - numpy
  - pandas
  - scipy

### Installation

For Ubuntu Linux users, install Supercell using:
```bash
sudo snap install supercell
```

## Protocol Steps

### 1. Rb Distribution

First, we distribute Rb atoms in their *32e* crystallographic site while keeping anions fixed.

```bash
# Create output directory
mkdir step-1_Rb_dist

# Generate configurations with 0.6 Å tolerance
supercell -i RbNb2O5F.cif -v 2 -m -t 0.6 -q -p "r(O[1]):fixed" -p "r(F[1]):fixed" -n l5 -o step-1_Rb_dist/1st_step
```

Note: The 0.6 Å tolerance is crucial due to Rb atoms being in the *32e* crystallographic site. Only lowest energy structures are considered to avoid Rb atom clustering.

### 2. Anion Distribution

For each of the 5 lowest energy CIFs from step 1, distribute anions in their *48f* crystallographic site:

```bash
# Create output directory
mkdir step-2_OF_dist

# Generate configurations for each Rb configuration
supercell -i step-2_OF_dist/Rb_config-1/1st_step_il00011252_w96.cif -v 2 -m -q -n l10000 -n h10000 -o step-2_OF_dist/Rb_config-1/2nd_step
supercell -i step-2_OF_dist/Rb_config-2/1st_step_il00011748_w96.cif -v 2 -m -q -n l10000 -n h10000 -o step-2_OF_dist/Rb_config-2/2nd_step
supercell -i step-2_OF_dist/Rb_config-3/1st_step_il00011751_w192.cif -v 2 -m -q -n l10000 -n h10000 -o step-2_OF_dist/Rb_config-3/2nd_step
supercell -i step-2_OF_dist/Rb_config-4/1st_step_il00016402_w12.cif -v 2 -m -q -n l10000 -n h10000 -o step-2_OF_dist/Rb_config-4/2nd_step
supercell -i step-2_OF_dist/Rb_config-5/1st_step_il00055815_w12.cif -v 2 -m -q -n l10000 -n h10000 -o step-2_OF_dist/Rb_config-5/2nd_step
```

## Data Analysis

### Analysis of [NbO<sub>6-x</sub>F<sub>x</sub>]<sup>n-</sup> Octahedral Populations

1. Run analysis scripts for each configuration:
```bash
# For lowest energy configurations
python3 code_configs_NbX6_l.py
sed -i "s/config-1/config-2/g" code_configs_NbX6_l.py
# Repeat for configs 2-5

# For highest energy configurations
python3 code_configs_NbX6_h.py
sed -i "s/config-1/config-2/g" code_configs_NbX6_h.py
# Repeat for configs 2-5
```

2. Concatenate output files:
```bash
python3 code_concatinate_NbX6_l.py
python3 code_concatinate_NbX6_h.py
```

### Visualization and Analysis

1. Plot Ewald energy distribution:
```bash
python3 Ewald_energy_dist.py
```
This generates `plot_ewald_dist.pdf` showing the distribution of Ewald energies vs. structure count.

2. Plot octahedral population distribution:
```bash
python3 prob_dist_NbX6.py
```
This script generates probability distributions for [NbO<sub>6-x</sub>F<sub>x</sub>]<sup>n-</sup> populations, comparing generated configurations with experimental data.

### Analysis of [RbO<sub>18-y</sub>F<sub>y</sub>]<sup>m-</sup> Populations

The same procedure used for [NbO<sub>6-x</sub>F<sub>x</sub>]<sup>n-</sup> analysis is applied to analyze [RbO<sub>18-y</sub>F<sub>y</sub>]<sup>m-</sup> populations, excluding the Ewald energy distribution plot.

## Output Files Structure

```
.
├── step-1_Rb_dist/
│   └── 1st_step/
├── step-2_OF_dist/
│   ├── Rb_config-1/
│   │   ├── oct_step-2_OF_dist_Rb_config-1_summary_l.csv
│   │   └── oct_step-2_OF_dist_Rb_config-1_summary_h.csv
│   ├── [Rb_config-2 through Rb_config-5]/
│   ├── concatenated_configs_NbX6_l.csv
│   └── concatenated_configs_NbX6_h.csv
├── plot_ewald_dist.pdf
└── [other generated plots]
```
---

For further details, please refer to the respective folders or contact the author via the provided email.

# Simulation of the theoretical NMR Spectra of RbM<sub>2</sub>O<sub>5</sub>F (M = Nb, Ta) Pyrochlore-type Oxyfluorides

**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains Python scripts for simulating theoretical <sup>19</sup>F, <sup>87</sup>Rb, and <sup>93</sup>Nb NMR spectra of RbNb<sub>2</sub>O<sub>5</sub>F and RbTa<sub>2</sub>O<sub>5</sub>F pyrochlore-type oxyfluorides using the `mrsimulator` package.

## Repository Structure

### RbNb<sub>2</sub>O<sub>5</sub>F
```
./RbNb2O5F/
├── 19F/
├── 87Rb/1D/
└── 93Nb/1D/
```

### RbTa<sub>2</sub>O<sub>5</sub>F
```
./RbTa2O5F/
├── 19F/
└── 87Rb/1D/
```

Each directory contains:
- `code_simulate.py`: Python script for simulating an NMR spectrum
- `exp_vs_fit_spec_and_model_all_lines.asc`: Experimental data
- GIPAW calculation files:
  - For RbNb<sub>2</sub>O<sub>5</sub>F: `models_2-3-4-8-9_<N>.gipaw` (N = F, Rb, Nb)
  - For RbTa<sub>2</sub>O<sub>5</sub>F: `models_2-4-7-8-9_<N>.gipaw` (N = F, Rb)

## Prerequisites

Required Python packages:
- [mrsimulator](https://github.com/deepanshs/mrsimulator)
- matplotlib
- pandas

## Usage

1. Navigate to the desired directory:
```bash
cd ./path/to/simulation/directory
```

2. Run the simulation script:
```bash
python3 code_simulate.py
```

## Simulation Process

The simulation workflow:
1. Reads experimental NMR data from `exp_vs_fit_spec_and_model_all_lines.asc`
2. Imports GIPAW calculation results for the specific nucleus
3. Uses mrsimulator to generate theoretical NMR spectra
4. Compares simulated spectra with experimental data

---

For further details, please refer to the respective folders or contact the author via the provided email.

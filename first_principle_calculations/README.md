# RbM<sub>2</sub>O<sub>5</sub>F (M = Nb, Ta) Geometry Optimization and NMR Parameters Calculations
**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains datasets from DFT calculations performed to optimize the short-range structures of RbM<sub>2</sub>O<sub>5</sub>F (M = Nb, Ta) and to compute their NMR parameters.

## Overview of the Data

The dataset includes both **inputs** (located in the folders: `INPUT_files`) and **outputs** (located in the folders: `OUTPUT_files`) for the following calculations:

1. **Atomic Position Optimization (APO) of Unit Cell Tested Configurations n°1-20:**  
   **Folder:** `./RbNb2O5F/uc-APO` and `./RbTa2O5F/uc-APO`

2. **NMR Parameter Calculations for the Unit Cell Tested Configurations n°1-20:**  
   **Folder:** `./RbNb2O5F/uc-APO_NMR` and `./RbTa2O5F/uc-APO_NMR`

3. **Atomic Position Optimization (APO) of 2 × 2 × 2 Supercell Tested Cofigurations n°1-10:**  
   **Folder:** `./RbNb2O5F/sc-APO` and `./RbTa2O5F/sc-APO`

4. **NMR Parameter Calculations for the 2 × 2 × 2 Supercell Tested Cofigurations n°1-10:**  
   **Folder:** `./RbNb2O5F/sc-APO_NMR` and `./RbTa2O5F/sc-APO_NMR`
   
The `.slurm` files (named `<name>_jv_oz.slurm`, where `name` corresponds to each calculation) and the `.log` files (named `<name>_vasp_run.log`) can be found in the folders [RbNb<sub>2</sub>O<sub>5</sub>F](./RbNb2O5F) and [RbTa<sub>2</sub>O<sub>5</sub>F](./RbTa2O5F).

## Methods

### APO of the Unit Cell Tested Configurations n°1-20 using `VASP`

The first-priciple calculations were performed using the **VASP** code (version 6.2.1). The periofic boundaries conditioned (PBC) **density functional theory (DFT)** approach used a wave function expanded on a plane-wave basis set, with a **550 eV** kinetic energy cut-off and a **(3 × 3 × 3)** shifted Monkhorst-Pack k-point mesh. The ground-state electronic structure was obtained by **the generalized gradient approximation (GGA)** using **the Perdew–Burke–Ernzerhof (PBE)** functional **(PBE-GGA)**. The interactions between core and valence electrons were treated using the **projector augmented wave (PAW)** method, incorporating the following PAW potentials and core electronic configurations:

- **O:** *O_s_GW*, core configuration: [He] 2s<sup>2</sup> 2p<sup>4</sup>
- **F:** *F_GW*, core configuration: [He] 2s<sup>2</sup> 2p<sup>5</sup>
- **Rb:** *Rb_sv_GW*, core configuration: [Kr] 5s<sup>1</sup>
- **Nb:** *Nb_sv_GW*, core configuration: [Ar] 4s<sup>2</sup> 4p<sup>6</sup> 4d<sup>5</sup>
- **Ta:** *Ta_sv_GW*, core configuration: [Xe] 5s<sup>2</sup> 5p<sup>6</sup> 5d<sup>5</sup>

Atomic positions were relaxed until forces converged to less than **0.1 meV/Å**, and total energy convergence was set to below **10<sup>–8</sup> eV**.

### APO of the 2 × 2 × 2 Supercell Tested Cofigurations n°1-10 using `CP2K`

The first-principles calculations were performed using the **CP2K** code (version ***?.?.?***). The PBC **density functional theory (DFT)** approach used a wave function expanded on a TZVP Gaussian basis set (MOLOPT library), with a charge density plane-wave expansion energy cutoff of **720 Ry**. The ground-state electronic structure was obtained by **PBE-GGA**. The interactions between core and valence electrons were treated using the Goedecker-Teter-Hutter (GTH) pseudo-potentials.

### NMR Parameters Calculations (uc-APO_NMR and sc-APO_NMR) using `VASP`

The **PAW** and **gauge including projector augmented wave (GIPAW)** methods were used to compute quadrupolar coupling NMR parameters (*C*<sub>Q</sub>, *η*<sub>Q</sub>) and magnetic shielding values (*σ*<sub>iso</sub>, *σ*<sub>CSA</sub>, *η*<sub>CSA</sub>) for both the unit cell and 2 × 2 × 2 supercell tested configurations. All parameters were set the same as those in the DFT relaxation process.

### Tensor Convention and Magnetic Shielding to Chemical Shift Conversion

Magnetic shielding tensors and experimental chemical shift parameters follow the **Haeberlen convention**. Definitions include:

- **Isotropic magnetic shielding (*σ*<sub>iso</sub>):** *σ*<sub>iso</sub> = (*σ*<sub>xx</sub> + *σ*<sub>yy</sub> + *σ*<sub>zz</sub>)/3  
- **Anisotropy of magnetic shielding (*σ*<sub>CSA</sub>):** *σ*<sub>CSA</sub> = *σ*<sub>zz</sub> – *σ*<sub>iso</sub>  
- **Asymmetry parameter (*η*<sub>CSA</sub>):** *η*<sub>CSA</sub> = (*σ*<sub>yy</sub> – *σ*<sub>xx</sub>)/*σ*<sub>CSA</sub>

In this study, NMR chemical shift values (*δ*<sub>iso</sub>) for **<sup>93</sup>Nb** were obtained from established linear regressions. For **<sup>19</sup>F** and **<sup>87</sup>Rb**, new linear regressions were established in this work.

## Directory Structure

The following directories contain the datasets:

- **RbNb<sub>2</sub>O<sub>5</sub>F Datasets:**
  - [uc-APO INPUT files](./RbNb2O5F/uc-APO/INPUT_files)
  - [uc-APO OUTPUT files](./RbNb2O5F/uc-APO/OUTPUT_files)
  - [uc-APO_NMR INPUT files](./RbNb2O5F/uc-APO_NMR/INPUT_files)
  - [uc-APO_NMR OUTPUT files](./RbNb2O5F/uc-APO_NMR/OUTPUT_files)
  - [sc-APO INPUT files](./RbNb2O5F/sc-APO/INPUT_files)
  - [sc-APO OUTPUT files](./RbNb2O5F/sc-APO/OUTPUT_files)
  - [sc-APO_NMR INPUT files](./RbNb2O5F/sc-APO_NMR/INPUT_files)
  - [sc-APO_NMR OUTPUT files](./RbNb2O5F/sc-APO_NMR/OUTPUT_files)

- **RbTa<sub>2</sub>O<sub>5</sub>F Datasets:**
  - [uc-APO INPUT files](./RbTa2O5F/uc-APO/INPUT_files)
  - [uc-APO OUTPUT files](./RbTa2O5F/uc-APO/OUTPUT_files)
  - [uc-APO_NMR INPUT files](./RbTa2O5F/uc-APO_NMR/INPUT_files)
  - [uc-APO_NMR OUTPUT files](./RbTa2O5F/uc-APO_NMR/OUTPUT_files)
  - [sc-APO INPUT files](./RbTa2O5F/sc-APO/INPUT_files)
  - [sc-APO OUTPUT files](./RbTa2O5F/sc-APO/OUTPUT_files)
  - [sc-APO_NMR INPUT files](./RbTa2O5F/sc-APO_NMR/INPUT_files)
  - [sc-APO_NMR OUTPUT files](./RbTa2O5F/sc-APO_NMR/OUTPUT_files)

## Requirements

The calculations in this folder were performed on the **IMMM cluster** in Le Mans Université using the **charger (node with 48 CPUs and 192Go memory)**. To run the calculations in this folder, you will need:

- **VASP** installed on your local machine or accessible on a supercomputer cluster (more information about **VASP** can be found in [VASP - website](https://www.vasp.at/)).
- A compatible **CPU** (e.g., Intel or AMD) with sufficient computational resources for running DFT calculations.
- The job batch script is configured for the SLURM workload manager and includes specifications for nodes, tasks, runtime, memory, and other settings. Modify the script to suit your specific calculation needs.

---

For further details, please refer to the respective folders or contact the author via the provided email.

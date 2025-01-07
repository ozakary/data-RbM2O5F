# Solid-State Nuclear Magnetic Resonance (ssNMR) Spectroscopy of RbNb<sub>2</sub>O<sub>5</sub>F (M = Nb, Ta)
Author: Ouail Zakary  
ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
E-mail: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
Website: [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This folder contains the solid-state nuclear magnetic resonance (ssNMR) spectroscopy data for the compounds **RbNb<sub>2</sub>O<sub>5</sub>F** and **RbTa<sub>2</sub>O<sub>5</sub>F**, recorded for the nuclei **<sup>19</sup>F**, **<sup>87</sup>Rb**, and **<sup>93</sup>Nb**.

## Overview of the Data
The dataset is divided into two main folders for **RbNb<sub>2</sub>O<sub>5</sub>F** and **RbTa<sub>2</sub>O<sub>5</sub>F**, with subfolders for each nucleus. The NMR spectra were recorded and fitted using Bruker TopSpin and DMFit software, respectively.

### Folders and Data Structure
1. **RbNb<sub>2</sub>O<sub>5</sub>F**
   - **<sup>19</sup>F Nucleus:**  
     Path: [./RbNb2O5F/19F](./RbNb2O5F/19F)  
     Fit File: [1R.fxml](./RbNb2O5F/19F/43/pdata/1/1R.fxml)
   
   - **<sup>87</sup>Rb Nucleus:**  
     Path to the MAS NMR spectrum: [./RbNb2O5F/87Rb](./RbNb2O5F/87Rb/mas_nmr)  
     The corresponding fit file: [1R.fxml](./RbNb2O5F/87Rb/mas_nmr/3/pdata/1/1R.fxml)

     Path to the 3QMAS NMR spectrum: [./RbNb2O5F/87Rb](./RbNb2O5F/87Rb/3qmas_nmr)  
     The corresponding fit file: [1R.fxml](./RbNb2O5F/87Rb/3qmas_nmr/3/pdata/1/1R.fxml)
 
   - **<sup>93</sup>Nb Nucleus:**  
     Path to the MAS NMR spectrum: [./RbNb2O5F/93Nb](./RbNb2O5F/93Nb/mas_nmr)  
     The corresponding fit file: [1R.fxml](./RbNb2O5F/93Nb/mas_nmr/210/pdata/20/1R.fxml)

     Path for the 3QMAS NMR spectrum: [./RbNb2O5F/93Nb](./RbNb2O5F/93Nb/3qmas_nmr)  
     The corresponding fit file: [1R.fxml](./RbNb2O5F/93Nb/3qmas_nmr/210/pdata/20/1R.fxml)

2. **RbTa<sub>2</sub>O<sub>5</sub>F**
   - **<sup>19</sup>F Nucleus:**  
     Path: [./RbTa2O5F/19F](./RbTa2O5F/19F)  
     Fit File: [1R.fxml](./RbTa2O5F/19F/1/pdata/1/1R.fxml)
   
   - **<sup>87</sup>Rb Nucleus:**  
     Path to the MAS NMR spectrum: [./RbTa2O5F/87Rb](./RbTa2O5F/87Rb/mas_nmr)  
     The corresponding fit file: [1R.fxml](./RbTa2O5F/87Rb/mas_nmr/3/pdata/1/1R.fxml)

     Path to the 3QMAS NMR spectrum: [./RbTa2O5F/87Rb](./RbTa2O5F/87Rb/3qmas_nmr)  
     The corresponding fit file: [1R.fxml](./RbTa2O5F/87Rb/3qmas_nmr/3/pdata/1/1R.fxml)

### Methods
**<sup>19</sup>F (I = 1/2) MAS NMR** spectra were recorded with a Bruker Avance III spectrometer functioning at 20.0 T (Larmor frequency of 800 MHz) using a 1.3 mm CP-MAS probe-head, the spinning frequency was set to 46 kHz. The Hahn echo sequence was used with an interpulse delay of one rotor period and a recycle delay of 300 s and 30 s for RbNb2O5F and RbTa2O5F, respectively. The 90° pulse was set to 1.56 µs (RF field of 160 kHz) and 1.25 µs (RF field of 200 kHz) for RbNb2O5F and RbTa2O5F, respectively.

**<sup>87</sup>Rb (I = 3/2) MAS and multiple-quantum MAS (MQMAS) NMR** spectra were acquired using a Bruker Avance III spectrometer operating at 20.0 T (Larmor frequency of 278.2 MHz). The spectra were recorded using a 2.5 mm CP-MAS probe-head, at a 30 kHz spinning frequency. The one-pulse MAS NMR spectra were recorded with a recycle delay of 0.25 s and a pulse duration of 0.38 µs (RF field of 64 kHz), corresponding to a small flip angle of 10° to ensure a total excitation of the entire spin system. The two-dimensional z-filtered MQMAS spectra were recorded using an RF field strength of 64 kHz for the triple-quantum excitation and reconversion (3QMAS), with a z-filter duration of 33 µs, recycle delay of 0.33 s and 128 t<sub>1</sub> increments with 1152 transients each. The duration of the central transition (CT) 90° selective pulse was set to 9.8 µs (RF field of 13 kHz).

**<sup>93</sup>Nb (I = 9/2) MAS and multiple-quantum MAS (MQMAS) NMR** spectra were acquired using a Bruker Avance III spectrometer operating at 20.0 T (Larmor frequency of 208.1 MHz). The spectra were recorded using a 0.7 mm CP-MAS probe-head, at an ultra-high spinning frequency of 100 kHz. The Hahn echo sequence was used for the one-dimensional CT MAS NMR spectrum (CTMAS), with a recycle delay of 1 s and duration of the CT 90° selective pulse of 2 µs (RF field of 25 kHz). The 3QMAS spectrum was acquired with an RF field strength of 350 kHz for the triple-quantum excitation and reconversion, a CT selective pulse of 2 µs (RF field of 25 kHz), a z-filter duration of one rotor period and a recycle delay of 0.5 s. 40 t<sub>1</sub> increments of 4800 transients each were accumulated.

**References:**  
- **<sup>19</sup>F** spectra were referenced to CFCl<sub>3</sub>.  
- **<sup>87</sup>Rb** spectra were referenced to a 1 M RbCl aqueous solution.  
- **<sup>93</sup>Nb** spectra were referenced to a saturated K[NbCl<sub>6</sub>]/CH<sub>3</sub>CN solution.

### Data Analysis
The raw ssNMR data was processed using **Bruker TopSpin** software and fitted using **DMFit**. The fitting files (`1R.fxml`) for each experiment are provided in their respective directories, and the fits can be visualized using DMFit.

### Raw Data and Fits:
- **RbNb<sub>2</sub>O<sub>5</sub>F:**
  - <sup>19</sup>F: [Raw Data and Fit](./RbNb2O5F/19F)
  - <sup>87</sup>Rb: [Raw Data and Fit](./RbNb2O5F/87Rb)
  - <sup>93</sup>Nb: [Raw Data and Fit](./RbNb2O5F/93Nb)
  
- **RbTa<sub>2</sub>O<sub>5</sub>F:**
  - <sup>19</sup>F: [Raw Data and Fit](./RbTa2O5F/19F)
  - <sup>87</sup>Rb: [Raw Data and Fit](./RbTa2O5F/87Rb)

### Requirements
To acquire, analyze, and visualize the ssNMR data, the following equipment and software are required:

- **Equipment Requirements:**
  - **Bruker Avance III** spectrometer 20 T or equivalent, along with the **CP-MAS probe-heads 0.7, 1.3, and 2.5 mm**.
  
- **Software Requirements:**
  - **Bruker TopSpin:** Required to process and visualize the raw NMR data. You can obtain the software from [Bruker's website](https://www.bruker.com/en/products-and-solutions/mr/nmr-software/topspin.html?s_kwcid=AL!14677!3!648890112603!p!!g!!nmr%20software%20free%20download&utm_source=Advertising&utm_medium=GoogleAd&utm_campaign=BBIO-Software-Cross-All-Software-H2-2024&gad_source=1&gclid=Cj0KCQjwgL-3BhDnARIsAL6KZ6-3cOPvJBH5UNxRvUrDug2NC94E8Bw_iE3Ey2GcHur_1z1SLIEYV5caApz2EALw_wcB).
  - **DMFit:** Required to fit the NMR spectra. The software is available for download at the [DMFit website](https://nmr.cemhti.cnrs-orleans.fr/).

---

For further details, please refer to the respective folders or contact the author via the provided email.

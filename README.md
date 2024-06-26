# Preparing NIHAO Simulation Output for Galactic Astronomy

**Github Repository:** https://www.github.com/svenbuder/preparing_NIHAO  
**Author:** Sven Buder (ANU, sven.buder@anu.edu.au) for this Github Repository. Simulation data is provided by NIHAO & Tobias Buck!

#### Simulation Data (cite these if you use the simulations!):
NIHAO-UHD simulations, see:  
[Buck (2020)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.5435B), [Buck et al. (2020b)](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491.3461B), [Buck et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.508.3365B), and [Buck et al. (2023)](https://ui.adsabs.harvard.edu/abs/2023MNRAS.523.1565B).

Also have a look at [Buder, Mijnarends, and Buck (2024)](https://ui.adsabs.harvard.edu/abs/2024arXiv240413835B), which uses the simulations for scientific exploration.

## Repository Content (without Larger NIHAO Simulation Files)

### Directory structure
```plaintext
nihao_simulation_analysis/
├── NIHAO_preparation.ipynb
├── NIHAO_raw/                      -> Raw Simulation output.  
├── NIHAO_prepared/                 -> Curated Simulations, as *gas.FITS and *stars.FITS.
└── example_exploration/
    └── nihao_spiral_arms/
        └── nihao_spiral_arms.ipynb -> example exploration of gas spiral arms and young stars
```

### Notebooks

#### `NIHAO_preparation.ipynb`:
This notebook is used to read the raw simulation output, convert properties, plot diagnostic plots, and create simpler FITS files for gas and stars each. It serves as a fundamental tool for preprocessing NIHAO simulation data before performing any detailed analysis.

#### `nihao_spiral_arms.ipynb`:
This notebook provides an example exploration of analyzing spiral arms in the NIHAO simulations. It demonstrates how to use the processed data to investigate specific structures within the simulation.

## Downloading Larger NIHAO Simulation Files:

The raw simulations are best retrieved via email enquiry.

Prepared FITS files for laypeople (aka Galactic astronomers) are publicly available for download at https://www.mso.anu.edu.au/~buder/NIHAO_prepared/.

There is a python file that loops through a wget command at NIHAO_prepared/download_NIHAO_prepared_FITS_files.py.

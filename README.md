# Spiral Simulation Study
## Intro
This repository contains the workflow documentation for a simulation study analyzing a spiral curl mechanism. The primary simulation work was conducted using Abaqus CAE. 

This study encompasses the entire process: from automating the model generation and job execution in Abaqus using Python, to extracting the resulting positional data. A core focus of the project is evaluating how accurately a theoretical spiral curl can be fitted to the actual path achieved and extracted from the simulation results. 

## Repository Structure

The repository is organized to separate simulation files, CAD models, and project documentation. The overall structure is visualized below:

    Spiral_Simulation_Study/
    ├── README.md
    ├── Spiral_Simulation_Report.pdf     (Must read)
    ├── Weekly_Summary.pdf               (Important)
    ├── Abaqus_files/
    ├── SolidWorks_files/
    ├── Literature/
    └── Documentation/

## Directory Details

### Root Level Files
* **Final_Report.pdf**: Comprehensive final document detailing every aspect of the simulation study, methodology, and conclusions.
* **Weekly_Summary_Report.pdf**: An informal, chronological log summarizing the weekly progress, challenges, and incremental findings throughout the study.

### 1. Abaqus Files
This folder contains the core simulation data and scripts:
* **Automation Script**: A Python program designed to automate the model setup and job creation directly within Abaqus CAE.
* **Exported Data**: The raw positional data extracted from the completed simulation studies.
* **Interactive Plotter**: A Python tool featuring a slider interface. This allows the user to scrub through specific time steps and visualize the 2D positional changes of the quadrilaterals.

### 2. Solidworks Files
This directory houses the initial geometric planning and parameter selection:
* **Quadrilateral Sketches**: Individual CAD sketches used to determine and establish the foundational parameters at the beginning of the study.
* **Parameter Logs**: Files with the chosen coordinates and parameter values.
* **Assembly Model**: An assembly to visualize how the individual components physically come together.

### 3. Literature
This folder contains the foundational work that guided my study:
* **Reference Papers**: Two primary academic research papers relevant to the mechanism.
* **Previous Technical Report**: An earlier technical report on this topic, which served as the baseline for the simulation study. (Important)

### 4. Documentation
This folder has the visual and analytical progress of the project:
* **Visualizations**: Video recordings exported from the Abaqus simulation study.
* **Progress Tracking**: Weekly summary slides and supporting Word documents.
* **Path Fitting Script**: A Python script used to plot the exported Abaqus data, fitting it mathematically to the spiral curl formula, and determine the final parameter values.
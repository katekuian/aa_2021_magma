# Team Magma - Analytics & Applications Team Assignment

Welcome to the git repository for the team assignment of Team Magma.  
This project is part of the the course Analytics and Applications (AA) from the University of Cologne and investigates bike sharing in Los Angeles in 2019.  
The project focus on two core aspects: **system monitoring** and **demand prediction**.

## Setup

The data that we analysed is not part of the repository, but to run the notebooks it is necessary to put the files `la_2019.csv` and `weather_hourly_la.csv` in the folder `00_data`.

## Repository Structure

To fulfill the data analysis and prediction tasks we will use python as a programming language. Our code will be writen in Jupyter Notebooks (.ipynb files).  
These notebooks are contained in the folders `01_data_collection_and_preparation`, `02_descriptive_analytics`, `03_cluster_analysis`, `04_predictive_analytics`.  
The results of our data preperation will be saved together with the original data files in the folder `00_data`.
Any documents, for example our report, are contained in the folder `documents`.

## `runall.py` script

To work on the tasks collaboratively we will use different branches for each task.  
Sometimes changes require a re-run of all notebooks. Therefore we created a `runall.py` script that runs all notebooks in the repository.
To only run notebooks in `01_data_collection_and_preparation` use the `--only-preperation` flag.
To specify a jupyter kernel to use add the `--kernel=<kernel>` flag. Note that you can find the names of your kernels with the command `jupyter kernelspec list`.

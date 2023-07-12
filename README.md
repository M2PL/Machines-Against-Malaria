# Machines against malaria
This code corresponds to the work done by M2PL in building ABS and dual-activity prediction models. Code relating to cluster-based undersampling, chemical space visualization, model building and evaluation are contained within the respective folders and the datasets for scripts are available in the Databases folder.

## Requirements
Create a conda environment using the following command:

```bash
cd machines-against-malaria
conda env create -f environment.yml
conda activate mam
```
##This is WIP, the environment file does not contain all the necessary dependencies

## Run predictions
You can run predictions for a single molecule by using the 'predict.py' script:

```bash
cd machines-against-malaria/Models
python ../src/predict.py <"your molecule"> <model_name>
```
###This is WIP, just a quick way of loading models outside the notebook



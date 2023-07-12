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

## License
MIT License

Copyright (c) 2023 M2PL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

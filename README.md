# Trials of the Dash library

## Contents
<!-- This contents is kept up to date *manually* -->
1. [Important notes](#important-notes)
1. [Setup](#setup)
    - [One-time setup](#one-time-setup)
    - [Run examples](#run-examples)
1. [Structure of the repo](#structure-of-the-repo)
1. [Tasks](#tasks)
    - [Manually download data](#manually-download-data)
    - [Run linting](#run-linting)
1. [References and further resources](#references-and-further-resources)

<div align="right"><a href="#contents">Back to Contents</a></div>

## Important notes
Following the instructions documented in this project to install and use the code is *at own risk*. See the project's [LICENSE](LICENSE).

<p align="right"><a href="#contents">Back to Contents</a></p>

## Setup
This package was developed in Visual Studio Code (VSCode) and Jupyter Notebooks. All console commands are **run from the root folder of this project** unless otherwise stated.

### One-time setup
Software prerequisites: `git` and `conda`.

1. Clone the Git repo:
    ```
    git clone [location of remote repo]
    ```
1. Recreate the conda environment:
    ```
    conda env create -f environment.yml --force
    ```
1. [*Optional*] Trigger a build of JupyterLab (or alternatively you will be prompted to do this on starting JupyterLab):
    ```
    jupyter lab build
    ```

### Run examples
Each time you want to start it up:
- VSCode: Should recognise the correct conda environment when you open the project.
- Jupyter Notebooks:
    ```
    conda activate dash_trials_env
    start jupyter notebook
    ```

<p align="right"><a href="#contents">Back to Contents</a></p>

## Structure of the repo
- `README.md`: Main introduction to the project.
- `data/`: No data files are committed to the repo. See `data\README.md` for instructions to manually download the data files from online sources that are used in some of the examples.
- `datacamp_tutorial/`: Working through the 'Dash for Beginners' article on DataCamp (see below for link).
- `environment.yml`: Specification of environment so it can be reproduced.
- `proj_config.py`: Central store of variables that can be referenced throughout the project.
- `.vscode/`: IDE settings, e.g. for common development tasks.
- `LICENSE`: Terms of use.

<p align="right"><a href="#contents">Back to Contents</a></p>

## Tasks
### Manually download data
No data files are committed to the repo. Some examples use external data from online sources. See `data\README.md` for details, where to get the data, and where to save it in the repo.

### Run an app
1. Open a Terminal in the project's root directory:
    ```
    conda activate dash_trials_env
    start python datacamp_tutorial\app_ex01_first_dashboard.py
    ```
    - Adding `start` at the beginning opens it in a separate Command Prompt
2. Then go to the IP address, e.g.: <http://127.0.0.1:8050/>
3. Stop it by `Ctrl + C` in the Terminal

### Run linting
To check code formatting using `pylint`.
```
pylint datacamp_tutorial/
```

<p align="right"><a href="#contents">Back to Contents</a></p>

## References and further resources
### Tutorials
- Dash official docs: <https://dash.plotly.com/>
    - Tutorial: <https://dash.plotly.com/installation>
- DataCamp article to get started with Dash: <https://www.datacamp.com/community/tutorials/learn-build-dash-python>

### Extensions
- dash-bootstrap-components package: <https://dash-bootstrap-components.opensource.faculty.ai/>
- Start a Dash app from Jupyter Lab using JupyterDash: <https://github.com/plotly/jupyter-dash>
    - Example here: <https://stackoverflow.com/a/63729413>
    - Also here: <https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e>

<div align="right"><a href="#contents">Back to Contents</a></div>

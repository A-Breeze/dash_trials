# Trials of the Dash library

## Contents
<!-- This contents is kept up to date *manually* -->
1. [Important notes](#important-notes)
1. [Setup](#setup)
    - [One-time setup](#one-time-setup)
    - [Run examples](#run-examples)
1. [Structure of the repo](#structure-of-the-repo)
1. [References and further resources](#references-and-further-resources)

<div align="right"><a href="#contents">Back to top</a></div>

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
    conda activate shap_example_env
    start jupyter notebook
    ```

<p align="right"><a href="#contents">Back to Contents</a></p>

## Structure of the repo
- `README.md`: Main introduction to the project.
- `datacamp_tutorial/`: Working through the 'Dash for Beginners' article on DataCamp (see below for link).
- `environment.yml`: Specification of environment so it can be reproduced.
- `.vscode/`: IDE settings, e.g. for common development tasks.
- `LICENSE`: Terms of use.

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

<div align="right"><a href="#contents">Back to top</a></div>

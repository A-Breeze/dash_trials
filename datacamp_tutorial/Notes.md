# 'Dash for Beginners' DataCamp article - Notes
Not part of the tutorial, just recording observations as I work through it.

## Contents
<!-- This contents is kept up to date *manually* -->
1. [Tutorial notes](#Tutorial-notes)
1. [Setup](#Setup)
1. [Recreate plotly plots](#Recreate-plotly-plots): Example 1, Example 2


<div align="right"><a href="#Contents">Back to Contents</a></div>

# Tutorial notes
## Dash app components
1. Layout = What the app looks like
1. Interactivity = How it works


<div align="right"><a href="#Contents">Back to Contents</a></div>

# Setup

```python
# Set warning messages
import warnings
# Show all warnings in IPython
warnings.filterwarnings('always')
# Ignore specific warnings
warnings.filterwarnings(
    "ignore",
    message="`should_run_async` will not call `transform_cell` automatically in the future"
)
```

```python
# For development, allow the project modules to be reloaded every time they are used
%load_ext autoreload
```

```python
# Import built-in modules
import sys, os

# Import external modules
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

# Import project modules
# Allow modules to be imported relative to the project root directory
from pyprojroot import here
root_dir_path = here()
if not sys.path[0] == str(root_dir_path):
    sys.path.insert(0, str(root_dir_path))
import proj_config
%aimport proj_config
%autoreload 1

# Check they have loaded and the versions are as expected
expected_conda_env = 'dash_trials_env'
assert expected_conda_env in sys.executable, (
    f"Please use the *custom* conda env for this notebook: {expected_conda_env}"
)
assert sys.version_info[:3] == (3, 8, 5)
print(f"Python version:\t\t{sys.version}")
assert np.__version__ == '1.19.1'
print(f'numpy version:\t\t{np.__version__}')
assert pd.__version__ == '1.1.1'
print(f'pandas version:\t\t{pd.__version__}')
assert plotly.__version__ == '4.9.0'
print(f'plotly version:\t\t{plotly.__version__}')
assert dash.__version__ == '1.14.0'
print(f'dash version:\t\t{dash.__version__}')
assert dash_renderer.__version__ == '1.6.0'
print(f'dash_renderer version:\t{dash_renderer.__version__}')
assert html.__version__ == '1.0.3'
print(f'dash_renderer version:\t{html.__version__}')
assert dcc.__version__ == '1.10.2'
print(f'dash_core_components version:\t{dcc.__version__}')
```

```python
# Configuration variables
DATA_URL = (
    'https://gist.githubusercontent.com/chriddyp/'
    '5d1ea79569ed194d432e56108a04d188/raw/'
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'
    'gdp-life-exp-2007.csv'
)
data_filepath = proj_config.DATA_DIR_PATH / "gdp-life-exp-2007.csv"
if data_filepath.is_file():
    print("Correct: Data file is available for loading")
else:
    print(
        "Warning: Data file not yet available in that location\n"
        f"Please download it manually from here:\n{DATA_URL}"
    )
```

<div align="right"><a href="#Contents">Back to Contents</a></div>

# Recreate plotly plots
In the apps, the `figure` specifications for the plot are passed to the `app.layout` as a `dcc.Graph` object.

## Example 1

```python
# Code from the app.py
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
figure = {
    'data': [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    ],
    'layout': {
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'font': {
            'color': colors['text']
        }
    }
}
plotly.io.show(figure)
```

## Example 2
Display a scatter plot using `go.Scatter`.

```python
# Load data
df = pd.read_csv(data_filepath)

# Reasonableness checks
assert df.shape == (142, 6)
assert df.dtypes.equals(pd.Series({
    'Unnamed: 0': np.dtype('int64'),
    'country': np.dtype('O'),
    'continent': np.dtype('O'),
    'population': np.dtype('float64'),
    'life expectancy': np.dtype('float64'),
    'gdp per capita': np.dtype('float64')
}))
print("Correct: Loaded data has successfully passed the reasonableness checks")
```

```python
figure = {
    'data': [
        go.Scatter(
            x=df[df['continent'] == i]['gdp per capita'],
            y=df[df['continent'] == i]['life expectancy'],
            text=df[df['continent'] == i]['country'],
            mode='markers',
            opacity=0.8,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ) for i in df.continent.unique()
    ],
    'layout': go.Layout(
        xaxis={'type': 'log', 'title': 'GDP Per Capita'},
        yaxis={'title': 'Life Expectancy'},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        legend={'x': 0, 'y': 1},
        hovermode='closest'
    )
}
plotly.io.show(figure)
```

```python

```

<div align="right"><a href="#contents">Back to top</a></div>

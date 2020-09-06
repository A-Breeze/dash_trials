# 'Dash for Beginners' DataCamp article - Notes
Not part of the tutorial, just recording observations as I work through it.

## Contents
<!-- This contents is kept up to date *manually* -->
1. [Tutorial notes](#Tutorial-notes)
1. [Setup](#Setup)
1. [Recreate plotly plot](#Recreate-plotly-plot)


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
# Import built-in modules
import sys, os

# Import external modules
import plotly
import dash

# Check they have loaded and the versions are as expected
expected_conda_env = 'dash_trials_env'
assert expected_conda_env in sys.executable, (
    f"Please use the *custom* conda env for this notebook: {expected_conda_env}"
)
assert sys.version_info[:3] == (3, 8, 5)
print(f"Python version:\t\t{sys.version}")
assert plotly.__version__ == '4.9.0'
print(f'plotly version:\t\t{plotly.__version__}')
assert dash.__version__ == '1.14.0'
print(f'dash version:\t\t{dash.__version__}')
```

```python
# Other dash packages
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

assert dash_renderer.__version__ == '1.6.0'
print(f'dash_renderer version:\t{dash_renderer.__version__}')
assert html.__version__ == '1.0.3'
print(f'dash_renderer version:\t{html.__version__}')
assert dcc.__version__ == '1.10.2'
print(f'dash_core_components version:\t{dcc.__version__}')
```

<div align="right"><a href="#Contents">Back to Contents</a></div>

# Recreate plotly plot
In the app, the `figure` specifications for the plot are passed to the `app.layout` as a `dcc.Graph` object.

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

<div align="right"><a href="#contents">Back to top</a></div>

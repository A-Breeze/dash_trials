"""
Example 02: Dashboard with a scatter plot
"""

#########
# Setup #
#########
# Import built-in modules
import sys

# Import external modules
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Import project modules
# Allow modules to be imported relative to the project root directory
from pyprojroot import here
root_dir_path = here()
if not sys.path[0] == str(root_dir_path):
    sys.path.insert(0, str(root_dir_path))
import proj_config   # pylint: disable=import-error

# Initialise app object
app = dash.Dash()

# Configuration variables
data_URL = (
    'https://gist.githubusercontent.com/chriddyp/'
    '5d1ea79569ed194d432e56108a04d188/raw/'
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'
    'gdp-life-exp-2007.csv'
)
data_filepath = proj_config.DATA_DIR_PATH / "gdp-life-exp-2007.csv"
if data_filepath.is_file():
    print("Correct: Data file is available for loading")
else:
    raise FileNotFoundError(
        "\n\tWarning: Data file not yet available in that location."
        "\n\tPlease download it manually from here..."
        f"\n\t{data_URL}"
        "\n\t...and save it here:"
        f"\n\t{data_filepath}"
    )

#############
# Data prep #
#############
# Read data from online source
df = pd.read_csv(data_filepath)

##############
# App layout #
##############
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
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
    )
])

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server(debug=True)  # Set to 'debug' to avoid refreshing on every update

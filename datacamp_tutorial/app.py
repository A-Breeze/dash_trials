r"""
Adapted from 'Dash for Beginners' article on DataCamp here: 
<https://www.datacamp.com/community/tutorials/learn-build-dash-python>

To run the app:
1. Open a Terminal in the project's root directory:
    ```
    conda activate dash_trials_env
    python datacamp_tutorial\app.py
    ```
    - Add `start` at the beginning to open it in the new Command Prompt
2. Then go to the IP address, e.g.: <http://127.0.0.1:8050/>
3. Stop it by `Ctrl + C` in the Terminal

"""

#########
# Setup #
#########
# Import external packages
import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialise app object
app = dash.Dash()

##############
# App layout #
##############
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
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
    )
])

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server(debug=True)  # Set to 'debug' to avoid refreshing on every update

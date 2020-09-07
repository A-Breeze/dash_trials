"""Example 04: Dashboard with some core components"""

#########
# Setup #
#########
# Import external modules
import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialise app object
app = dash.Dash()

##############
# App layout #
##############
widget_layout = html.Div([
    html.Label('Default Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),
    html.Label('Text Box'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),
], style={'columnCount': 2})

app.layout = html.Div([
    html.H1(
        children='Hello Dash',
        style={'textAlign': 'center',}
    ),
    html.Div(
        children='Dash: A web application framework for Python.',
        style={'textAlign': 'center',}
    ),
    widget_layout
])

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server(debug=True)  # Set to 'debug' to avoid refreshing on every update

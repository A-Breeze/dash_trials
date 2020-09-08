"""Example 05: Dashboard including interactive components"""

#########
# Setup #
#########
# Import external modules
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialise app object
app = dash.Dash()

##############
# App layout #
##############
app.layout = html.Div([
    dcc.Input(id='my-id', value='Dash App', type='text'),
    html.Div(id='my-div')
])

#############
# Callbacks #
#############
@app.callback(
    # Result of function will go into the 'my_div' HTML element in the 'children' property
    output=Output(component_id='my-div', component_property='children'),
    # List of inputs that will trigger a change
    inputs=[
        # Watches the 'value' component of the 'my-id' dcc element
        Input(component_id='my-id', component_property='value')
    ],
    # state=()  # Items with additional info that do *not* trigger a callback
    # prevent_initial_call=False  # Option to *not* fire the callback when arguments are first added
)
def update_output_div(input_value):
    """Format the input string for displaying"""
    return 'You\'ve entered "{}"'.format(input_value)

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server()

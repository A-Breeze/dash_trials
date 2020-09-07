"""Example 06: App with basic authentication"""

#########
# Setup #
#########
# Import external modules
import dash
import dash_html_components as html
import dash_auth

# Initialise app object
app = dash.Dash()

##################
# Authentication #
##################
# Set authentication keys
VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world'],
    ['me', 'my_passwod'],
]

# Only allow authenticated access
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

##############
# App layout #
##############
app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={'textAlign': 'center',}
    ),
    html.Div(
        children='Congratulations! You\'ve entered the app',
        style={'textAlign': 'center',}
    ),
])

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server()

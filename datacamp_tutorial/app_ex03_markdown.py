"""Example 03: Dashboard with a markdown component"""

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
markdown_text = '''
### Dash and Markdown
A lot of text
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

###########
# Run app #
###########
if __name__ == '__main__':
    app.run_server()

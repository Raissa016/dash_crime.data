import dash
import dash_bootstrap_components as dbc


#from dash import app
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
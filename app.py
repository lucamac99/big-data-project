import dash 
import dash_bootstrap_components as dbc

FONT_AVESOME = ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

""" local """
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.COSMO, FONT_AVESOME], requests_pathname_prefix='/project/', routes_pathname_prefix='/project/')
server = app.server
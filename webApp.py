import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.DropdownMenuItem import DropdownMenuItem

from app import app

#import pages
import homepage
import rent
import price


dropdown_menu = dbc.DropdownMenu(
    children = [
        dbc.DropdownMenuItem("Rent", href="/project/rent"),
        dbc.DropdownMenuItem("Price", href="/project/price"),
    ],
    nav=True,
    in_navbar = True,
    label = "MENU"
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Logo123456.jpg/400px-Logo123456.jpg', height="50px")),
                        dbc.Col(dbc.NavbarBrand("Big Data Project", className="ms-2")),
                    ],
                    align="center",
                    className = "g-0",
                ),
                href="/project/",
                style={'textDecoration': "none"}
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    dropdown_menu,
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True
            ),
        ]
    ),
    sticky="top",
    color='#F39C12',
    className="mb-5"
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/project/':
        return homepage.layout
    if pathname == '/project/rent':
        return rent.layout   
    if pathname == '/project/price':
        return price.layout   
    else:
        return homepage.layout

if __name__ == '__main__':
    app.run_server(debug=False, port='8000') 

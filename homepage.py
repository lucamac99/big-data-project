import dash
from app import app
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

layout =  html.Div(
    [
        html.Div(
            [
                html.Div(style={'display':'inline-block', 'width':'40%'}),
                html.Div(
                    dbc.Row(
                        [
                            html.H1('PROJECT VIEW')
                        ]
                    ), style={'display':'inline-block', 'width':'20%', 'font-style':'bold', 'color':'#002A5E'}
                ),
                html.Div(style={'display':'inline-block', 'width':'40%'})
            ], style={'margin-top':35}
        ),
        html.Div(
            [
                html.Div(style={'display':'inline-block', 'width':'25%'}),
                html.Div(
                    [
                        html.Div(
                            dbc.Row(
                                [
                                    html.P('In this application is possibile to consult the follow stats:'),
                                    html.Li("(Rent) data on the rent price in Europe"),
                                    html.Li("(Price) data on the housing price in Europe"),

                                ]
                            ), style={'color':'#002A5E', 'fontSize':22}
                        ),
                        html.Div(
                            [
                                dbc.Button("Rent", color="primary", id='logistica_button',size="lg", n_clicks=0, href='/project/rent', className="me-1"), 
                                dbc.Button("Price", color="primary", id='logistica_button', size="lg",n_clicks=0, href='/project/price', className="me-1"),  
                            ],
                            style={'margin-top':25}
                        )
                    ], style={'display':'inline-block', 'width':'50%'}
                ),
                html.Div(style={'display':'inline-block', 'width':'25%'})
            ], style={'margin-top':35}
        ),
    ]
)
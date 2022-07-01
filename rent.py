from typing import Text
import dash 
import pandas
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import warnings
warnings.filterwarnings('ignore')
from dataCleaning import data_cleaning
import plotly.express as px
import plotly.graph_objs as go

from app import app

df_rent, df_rent_price, df_house_price = data_cleaning()

df_rent.groupby('country').mean()['index']

# -------------------------- LAYOUT DASH APP ---------------------------------
select_coutry = [
    html.Div(
        dcc.Dropdown(
            id='country', options=[{'label':c, 'value':c} for c in df_rent.country.unique()],
            placeholder='Select a country', value='Italy',
        ), style={'display':'inline-block', 'width':300}
    )
]

layout = html.Div(
    [
        html.Div(children=select_coutry, style={'margin-left':100, 'margin-right':100, 'margin-top':30, 'color':'#002A5E'}),
        html.Div([
            dcc.Graph(id='country_rent')], style={'margin-left': 50, 'margin-right':100}),
        html.Div(
            dcc.Graph(
                    id='rent-chart-2',
                    figure={
                        'data': [go.Bar(
                                x = df_rent['country'],
                                y = df_rent['index'],
                                )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
            ),
        ),
        html.Div(
            dbc.Row(
                [
                    html.Li('Plots'),
                ]
            ), style={'color':'#002A5E', 'fontSize':22, 'allign':'center'}
        ),
        html.Div([
            dbc.Row(
                    [
                        dbc.Col(html.Img(src='assets/rent_price.png')),
                        dbc.Col(html.Img(src='assets/rent_index_2020.png')),
                        dbc.Col(html.Img(src='assets/rent_price_compare.png')),
                        dbc.Col(html.Img(src='assets/rent_throw_years.png')),
                    ],
                    align="center",
                    className = "g-0",
                ),
        ])
    ]
)

# rent price chart
@app.callback(
    Output(component_id='country_rent', component_property='figure'),
    [Input(component_id='country', component_property='value')]
)
def grafico_country_rent(selected_country):
    df = df_rent[df_rent['country'] == selected_country]
    df_ordinato = df.groupby(['country']).mean()['index'].to_frame().reset_index()
    df_ordinato.columns = ['country', 'price', 'index', 'surface']

    
    fig = px.bar(df_ordinato, x='country', y='index', color='price',
                markers=True, title='Country: ' + selected_country)
    fig.add_traces(fig.data)
    return fig
from typing import Text
import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import html
import warnings
warnings.filterwarnings('ignore')
from dataCleaning import data_cleaning
import plotly.express as px
import plotly.graph_objs as go

from app import app

df_rent, df_rent_price, df_house_price = data_cleaning()


# -------------------------- LAYOUT DASH APP ---------------------------------
select_coutry = [
    html.Div(
        dcc.Dropdown(
            id='my-country', options=[{'label':c, 'value':c} for c in df_house_price['country']],
            placeholder='Select a country', value='Italy',
        ), style={'display':'inline-block', 'width':300}
    )
]

layout = html.Div(
    [
        html.Div(children=select_coutry, style={'margin-left':100, 'margin-right':100, 'margin-top':30, 'color':'#002A5E'}),
        html.Div([
            dcc.Graph(id='price-chart')], style={'margin-left': 50, 'margin-right':100}),
        html.Div(
            dcc.Graph(
                    id='price-chart-2',
                    figure={
                        'data': [go.Bar(
                                x = df_house_price['country'],
                                y = df_house_price['2020'],
                                )
                        ],
                        'layout': go.Layout(
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
        )),
        html.Div(
            dbc.Row(
                [
                    html.Li('Plots'),
                ]
            ), style={'color':'#002A5E', 'fontSize':25, 'allign':'center'}
        ),
        html.Div([
            dbc.Row(
                    [
                        dbc.Col(html.Img(src='assets/house_price.png')),
                        dbc.Col(html.Img(src='assets/house_index_2020.png')),
                        dbc.Col(html.Img(src='assets/bubble_chart.png')),
                    ],
                    align="center",
                    className = "g-0",
                ),
        ])
    ]
)

# house price housing chart
@app.callback(
    Output(component_id='price-chart', component_property='figure'),
    [Input(component_id='my-country', component_property='value')]
)
def grafico_country_rent(selected_country):
    df = df_house_price[df_house_price['country'] == selected_country]
    df.columns = ['country', '2020']
    fig = px.bar(df, x='country', y='2020', markers=True, title='Country: ' + selected_country)
    return fig
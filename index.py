from app import app
from app import server
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import dash_table

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app.layout = html.Div([html.H1('Dash Demo Graph - Sam',
                               style={
                                      'textAlign': 'center',
                                      "background": "red"}),



                dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict('records'),
                                                        ),



                       dcc.Graph(
                           id='graph-1',
                           figure={
                               'data': [
                                   {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [10, 20, 30, 40, 50, 60, 70], 'type': 'line', 'name': 'value1'},
                                   {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [12, 22, 36, 44, 49, 58, 73], 'type': 'line', 'name': 'value2'}
                               ],
                               'layout': {
                                   'title': 'Line Graph',
                                     }
                                 }
                            ),

                            ], style={
                                "background": "#000080"}
                         )

if __name__ == '__main__':
    app.run_server(debug=True)
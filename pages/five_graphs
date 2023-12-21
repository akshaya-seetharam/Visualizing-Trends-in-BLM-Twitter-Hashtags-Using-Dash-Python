import dash
from dash import html
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
from collections import defaultdict, Counter
from dash import Dash, dash_table
import datetime

dash.register_page(__name__,  order=2)


from dash import Dash, dash_table, dcc, html, Input, Output, callback
import pandas as pd

df = pd.read_excel('tweetdata.xlsx')
dfForMillion = df[['created_at', 'user', 'hashtags', 'text']]  # prune columns for example

dfForMillion2 = dfForMillion[:5000]

for i in range(len(dfForMillion2)):
    #spliting the time stamp to focus on day instead of time
    timestamp = dfForMillion2["created_at"][i]
    dfForMillion2["created_at"][i] = timestamp.split()[0]

print(dfForMillion2.head())


dfForMillion2['id'] = dfForMillion2['user']
dfForMillion2.set_index('id', inplace=True, drop=False)

#app = Dash(__name__)
#dfForMillion2 = dfForMillion2[['created_at', 'user', 'hashtags', 'text']]  # prune columns for example
#dfForMillion2.set_index('id', inplace=True, drop=False)

layout = html.Div([
    dash_table.DataTable(
        id='datatable-row-ids',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in dfForMillion2.columns
            # omit the id column
            if i != 'id'
        ],
        data=dfForMillion2.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-row-ids-container')
])


@callback(
    Output('datatable-row-ids-container', 'children'),
    Input('datatable-row-ids', 'derived_virtual_row_ids'),
    Input('datatable-row-ids', 'selected_row_ids'),
    Input('datatable-row-ids', 'active_cell'))

def update_graphs(row_ids, selected_row_ids, active_cell):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = dfForMillion2
        # pandas Series works enough like a list for this to be OK
        row_ids = dfForMillion2['created_at']
    else:
        dff = dfForMillion2.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['#FF69B4' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else '#0074D9'
              for id in row_ids]

    return [
        dcc.Graph(
            id=column + '--row-ids',
            figure={
                'data': [
                    {
                        'x': dff['created_at'],
                        'y': dff[column],
                        'type': 'bar',
                        'marker': {'color': colors},
                    }
                ],
                'layout': {
                    'xaxis': {'automargin': True},
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': column}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ['hashtags'] if column in dff
    ]

dash.register_page(
    __name__,
    path='/choice',
    title='Top 5 Common Hashtags',
    name='Displaying Trends for Common Hashtags'
)

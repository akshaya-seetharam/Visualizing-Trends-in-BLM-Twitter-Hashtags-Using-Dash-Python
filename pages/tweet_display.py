import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
from collections import defaultdict, Counter
from dash import Dash, dash_table
import datetime


df = pd.read_excel('tweetdata.xlsx')

df = df[['created_at', 'user', 'hashtags', 'text']]  # prune columns for example


dash.register_page(__name__, order=1)


for i in range(len(df)):
    #spliting the time stamp to focus on day instead of time
    timestamp = df["created_at"][i]
    df["created_at"][i] = timestamp.split()[0]

layout = html.Div([
    html.H1('Displaying all Available Tweets'),
    html.Div('Filter the data using a data or a specific hashtag for a closer look at the data.'),

    dash_table.DataTable(
    columns=[
        {'name': 'Date Tweeted', 'id': 'created_at', 'type': 'datetime'},
        {'name': 'Twitter ID', 'id': 'user', 'type': 'text'},
        {'name': 'Hashtags', 'id': 'hashtags', 'type': 'text'},
        {'name': 'Tweet', 'id': 'text', 'type': 'text'},
       # {'name': 'Mock Dates', 'id': 'Mock Date', 'type': 'datetime'}
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        #'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)])
dash.register_page(
    __name__,
    path='/all_tweets',
    title='Tweet Data',
    name='Displaying All Tweets'
)

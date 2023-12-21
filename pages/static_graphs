import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
from collections import defaultdict, Counter
from dash import Dash, dash_table
import datetime
import ast

from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# loads the "darkly" template and sets it as the default
load_figure_template("darkly")

dash.register_page(__name__, order=3)

df = pd.read_excel('tweetdata.xlsx')
df = df[['created_at', 'user', 'hashtags', 'text']]  # prune columns for example
#print(df.size)
#keeping track of count for hashtags
millHashtags = {}

for i in range(len(df)):
    current = df["hashtags"][i]
    res = ast.literal_eval(current)
    #print(type(res))
    for i in range(len(res)):
        if res[i] in millHashtags:
            millHashtags[res[i]] +=1
        else:
            millHashtags[res[i]] = 1

millCommonHashtags = []

for key in millHashtags:
    if millHashtags[key]>500 and key != 'newpost':
        millCommonHashtags.append(key)

print(millCommonHashtags)
hashtagsByDayMillion = defaultdict(Counter)
for i in range(len(df)):
    #spliting the time stamp to focus on day instead of time
    timestamp = df["created_at"][i]
    date = timestamp.split()[0]
    
    #getting list of hastags used in tweet
    allHashtags = df["hashtags"][i]
    res = ast.literal_eval(allHashtags)
    #incrementing counter for the hashtag if it is one of the most common hashtags
    for tag in res:
        if (tag in millCommonHashtags):
            hashtagsByDayMillion[tag][date] += 1
dfForMillion2 = pd.DataFrame.from_dict(hashtagsByDayMillion) 
fig = px.area(dfForMillion2, facet_col="variable", facet_col_wrap=3)

layout = html.Div([
    html.H4('Hashtags with 500+ Incurrences (July - August 2013)'),
    dcc.Graph(figure=fig)
])



dash.register_page(
    __name__,
    path='/common-hashtags',
    title='Top 5 Common Hashtags',
    name='Hashtags with 500+ Incurrences'
)

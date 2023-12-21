import dash
from dash import html
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import dash_mantine_components as dmc

import plotly.express as px

dash.register_page(__name__, order=4)

df2 = pd.read_excel('tweethashtags2.xlsx')
print(df2.head())

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# loads the "darkly" template and sets it as the default
load_figure_template("darkly")

from dash import Dash, dcc, html, Input, Output
import plotly.express as px


layout = html.Div([
    html.H4('Analysis of Hashtag Prevalence (July 2013 - August 2015)'),
    dcc.Dropdown(
        id="dropdown",
        options=['icantbreathe', 'ferguson',  'blm',  'mikebrown',  'blacklivesmatter','michaelbrown','ericgarner','justiceformikebrown','ripmikebrown','handsupdontshoot','darrenwilson',
                  'nypd', 'police','baltimore', 'policebrutality', 'tamirrice','freddiegray','baltimoreriots','baltimoreuprising','alllivesmatter',
 'sandrabland', 'trayvonmartin','sayhername', 'walterscott'],
        value=[],
        multi=True
    ),
    dcc.Graph(id="graph"),
    dmc.Timeline(
    [
        dmc.TimelineItem(
            [
                dmc.Anchor(
                    "Trayvon Martin, February 26, 2012",
                    href="https://www.npr.org/sections/codeswitch/2018/07/31/631897758/a-look-back-at-trayvon-martins-death-and-the-movement-it-inspired",
                    underline=False,
                ),
            ],
        ),
        dmc.TimelineItem(
            [          dmc.Anchor(
                    "Eric Garner, July 17, 2014",
                    href="https://www.nytimes.com/2015/06/14/nyregion/eric-garner-police-chokehold-staten-island.html",
                    underline=False,
                ),
            ],
        ),
        dmc.TimelineItem([
                dmc.Anchor(
                    "Michael Brown, Aug. 9, 2014",
                    href="https://www.history.com/this-day-in-history/michael-brown-killed-by-police-ferguson-mo",
                    underline=False,
                ),
            ],),
        dmc.TimelineItem([
                dmc.Anchor(
                    "Tamir Rice, Nov. 22, 2014",
                    href="https://exhibits.stanford.edu/saytheirnames/feature/tamir-rice",
                    underline=False,
                ),
            ],),
            dmc.TimelineItem([
                dmc.Anchor(
                    "Walter Scott, April 4, 2015",
                    href="https://www.pbs.org/newshour/tag/walter-scott",
                    underline=False,
                ),
            ],),
            dmc.TimelineItem([
                dmc.Anchor(
                    "Sandra Bland, July 13, 2015",
                    href="https://www.ebony.com/what-happened-to-sandra-bland-505/",
                    underline=False,
                ),
            ],),
    ],
    active=6,
)
])


@callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(dims):
    fig = px.line(
        df2, x = 'Dates', y = dims)
    return fig


dash.register_page(
    __name__,
    path='/graph',
    title='Hashtag Trends (July 2013 - August 2015)',
    name='Hashtag Tracker Over 2 Years'
)

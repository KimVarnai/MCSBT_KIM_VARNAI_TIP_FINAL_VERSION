from calendar import month
import dash
from dash import dcc
from dash import html

from flask_login.utils import login_required
import plotly.express as px
import pandas as pd




# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# df = pd.DataFrame(
#     {
#         "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#         "Amount": [4, 1, 2, 2, 4, 5],
#         "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
#     }
# )

from data_requests import get_kpi1, get_kpi2, get_kpi3, get_kpi4, get_kpi5, get_kpi6, get_kpi7, get_kpi8, get_kpi9,get_kpi10, get_kpi11, get_kpi12, get_kpi13, get_kpi14, get_kpi15, get_kpi16, get_kpi17

df_kpi1 = pd.DataFrame(get_kpi1()["items"])
df_kpi2 = pd.DataFrame(get_kpi2()["items"])
df_kpi3 = pd.DataFrame(get_kpi3()["items"])
df_kpi4 = pd.DataFrame(get_kpi4()["items"])
df_kpi5 = pd.DataFrame(get_kpi5()["items"])
df_kpi6 = pd.DataFrame(get_kpi6()["items"])
df_kpi7 = pd.DataFrame(get_kpi7()["items"])
df_kpi8 = pd.DataFrame(get_kpi8()["items"])
df_kpi9 = pd.DataFrame(get_kpi9()["items"])
df_kpi10 = pd.DataFrame(get_kpi10()["items"])
df_kpi11 = pd.DataFrame(get_kpi11()["items"])
df_kpi12 = pd.DataFrame(get_kpi12()["items"])
df_kpi13 = pd.DataFrame(get_kpi13()["items"])
df_kpi14 = pd.DataFrame(get_kpi14()["items"])
df_kpi15 = pd.DataFrame(get_kpi15()["items"])
df_kpi16 = pd.DataFrame(get_kpi16()["items"])
df_kpi17 = pd.DataFrame(get_kpi17()["items"])

# flask_app, title_name, data

# base = /dash/
# url_base_pathname= base + title_name


def create_dash_application(flask_app):
     #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/", external_stylesheets=['static/Login_v3/css/dash-app-stylesheets/dash-analytics-report.css'])

    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of incidences per month"),
            
            html.Div(
                children="""
            January to April 2021- incidence number per priority per month
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df_kpi1, x="month", y="incidence_code",color="priority", barmode="group")
            ),
            html.Div(
                children="""
            All incidences summed up per priority, colorcoded per month
        """
            ),
            dcc.Graph(
                id="example-graph-1",
                figure=px.histogram(df_kpi1, x="incidence_code", y="priority",color="month",)
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app
    

def create_dash_application_1(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash1/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of incidences solved per month"),
            html.Div(
                children="""
            Number of incidences solved per month easily comparable
        """
            ),
            dcc.Graph(
                id="example-graph-test2",
                figure=px.bar(df_kpi2, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Number of incidences solved per month whereas the numbers of the prior month flow into the next one
        """
            ),
            dcc.Graph(
                id="example-graph-test3",
                figure=px.line(df_kpi2, x="month", y="incident_code")
            ),
             html.Div(
                children="""
            Number of incidences solved comparable per month in percentage and towards the overall entity
        """
            ),
            dcc.Graph(
                id="example-graph-test300",
                figure=px.pie(df_kpi2, names="month", values="incident_code")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_2(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash2/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of critical incidences per month"),
            html.Div(
                children="""
            Number of critical incidences per month comparable visually
        """
            ),
            dcc.Graph(
                id="example-graph-test4",
                figure=px.bar(df_kpi3, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Number of critical incidences per month whereas the numbers of the prior month flow into the next one
        """
            ),
            dcc.Graph(
                id="example-graph-test5",
                figure=px.line(df_kpi3, x="month", y="incident_code")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_3(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash3/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Type of Incidences (their Causes)"),
            html.Div(
                children="""
            Number of incidences per incidence type
        """
            ),
            dcc.Graph(
                id="example-graph-test6",
                figure=px.bar(df_kpi4, x="incident_type", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Percentage of each incident type
        """
            ),
            dcc.Graph(
                id="example-graph-test7",
                figure=px.pie(df_kpi4, values="incident_code", names="incident_type")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_4(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash4/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of Critical incidences that meet SLA requirements"),
            html.Div(
                children="""
            Comparison of Critical incidences that were solved whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test8",
                figure=px.bar(df_kpi5, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of Critical incidences that were solved whilst meeting SLA requirements in percentages between each months
        """
            ),
            dcc.Graph(
                id="example-graph-test9",
                figure=px.pie(df_kpi5, values="incident_code", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_5(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash5/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of Alta incidences that meet SLA requirements"),
            html.Div(
                children="""
            Comparison of Alta incidences that were solved whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test10",
                figure=px.bar(df_kpi6, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of Alta incidences that were solved whilst meeting SLA requirements in percentages between each months
        """
            ),
            dcc.Graph(
                id="example-graph-test11",
                figure=px.pie(df_kpi6, values="incident_code", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_6(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash6/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of Media incidences that meet SLA requirements"),
            html.Div(
                children="""
            Comparison of Media incidences that were solved whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test12",
                figure=px.bar(df_kpi7, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of Media incidences that were solved whilst meeting SLA requirements in percentages between each months
        """
            ),
            dcc.Graph(
                id="example-graph-test13",
                figure=px.pie(df_kpi7, values="incident_code", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_7(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash7/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Number of Baja incidences that meet SLA requirements"),
            html.Div(
                children="""
            Comparison of Baja incidences that were solved whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test14",
                figure=px.bar(df_kpi8, x="month", y="incident_code", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of Baja incidences that were solved whilst meeting SLA requirements in percentages between each months
        """
            ),
            dcc.Graph(
                id="example-graph-test15",
                figure=px.pie(df_kpi8, values="incident_code", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_8(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash8/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average SLA time for critical incidents whilst meeting SLA requirements"),
            html.Div(
                children="""
            
        """
            ),
            dcc.Graph(
                id="example-graph-test16",
                figure=px.bar(df_kpi9, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            
        """
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_9(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash9/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed in hours broken down into types"),
            html.Div(
                children="""
            Average time elapsed in hours per type
        """
            ),
            dcc.Graph(
                id="example-graph-test18",
                figure=px.bar(df_kpi10, x="incident_type", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Average time per type compared to the other types and the AVG time as a whole
        """
            ),
            dcc.Graph(
                id="example-graph-test19",
                figure=px.pie(df_kpi10, values="average_time_elapsed", names="incident_type")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_10(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash10/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed when SLA requirements are met for priority Baja"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Baja incidences whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test20",
                figure=px.bar(df_kpi11, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Baja incidences whilst meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test21",
                figure=px.pie(df_kpi11, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_11(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash11/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed when SLA requirements are met for priority Media"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Media incidences whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test22",
                figure=px.bar(df_kpi12, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Media incidences whilst meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test23",
                figure=px.pie(df_kpi12, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_12(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash12/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed when SLA requirements are met for priority Alta"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Alta incidences whilst meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test24",
                figure=px.bar(df_kpi13, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Alta incidences whilst meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test25",
                figure=px.pie(df_kpi13, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_13(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash13/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed for Critical incidences"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Critical incidences whilst not necessarily meeting SLA requirement
        """
            ),
            dcc.Graph(
                id="example-graph-test26",
                figure=px.bar(df_kpi14, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Critical incidences whilst not necessarily meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test27",
                figure=px.pie(df_kpi14, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_14(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash14/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed for priority Alta not necessarily meeting SLA requirement"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed per month
        """
            ),
            dcc.Graph(
                id="example-graph-test28",
                figure=px.bar(df_kpi15, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve ALta incidences not necessarily meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test29",
                figure=px.pie(df_kpi15, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_15(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash15/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed for priority Media not necessarily meeting SLA requirement"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed per month
        """
            ),
            dcc.Graph(
                id="example-graph-test30",
                figure=px.bar(df_kpi16, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Media incidences not necessarily meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test31",
                figure=px.pie(df_kpi16, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

def create_dash_application_16(flask_app): 
    #data, title):

    # base = '/dash/'
    # url = base + title + "/"

    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash16/", external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Average time elapsed for priority Baja not necessarily meeting SLA requirement"),
            html.Div(
                children="""
            Comparison of the AVG time elapsed per month
        """
            ),
            dcc.Graph(
                id="example-graph-test32",
                figure=px.bar(df_kpi17, x="month", y="average_time_elapsed", barmode="group")
            ),
            html.Div(
                children="""
            Comparison of the AVG time elapsed to solve Baja incidences not necessarily meeting SLA requirement in percentage and in-between months
        """
            ),
            dcc.Graph(
                id="example-graph-test33",
                figure=px.pie(df_kpi17, values="average_time_elapsed", names="month")
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
    return dash_app

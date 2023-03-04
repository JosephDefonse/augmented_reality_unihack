# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css", dbc.themes.BOOTSTRAP])

navbar = dbc.Navbar(
    children=[
        dbc.Button("Order Now", outline=True, className="ms-4", id="btn_sidebar"),
        dbc.NavbarBrand("Eshaan's Kitchen", className="ms-3"),
    ],
    color="dark",
    dark=True,
)



SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 50,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 50,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.P(
            "Melbourne, VIC", className="lead"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("COCKTAILS", href="/cocktails", id="page-1-link"),
                dbc.NavLink("WINE", href="/wine", id="page-2-link"),
                dbc.NavLink("BEER & CIDER", href="/beer-and-cider", id="page-3-link"),
                dbc.NavLink("SPIRITS", href="/spirits", id="page-4-link"),
                dbc.NavLink("NON-ALCOHOLIC", href="/non-alcoholic", id="page-5-link"),
                dbc.NavLink("COLD DRINKS", href="/cold-drinks", id="page-6-link"),
                dbc.NavLink("HOT DRINKS", href="/hot-drinks", id="page-7-link"),
                dbc.NavLink("STARTERS", href="/starters", id="page-8-link"),
                dbc.NavLink("MAINS", href="/mains", id="page-9-link"),
                dbc.NavLink("BURGERS", href="/burgers", id="page-10-link"),
                dbc.NavLink("WRAPS", href="/wraps", id="page-11-link"),
                dbc.NavLink("SIDES", href="/sides", id="page-12-link"),
                dbc.NavLink("KIDS MENU", href="/kids-menu", id="page-13-link"),
                dbc.NavLink("DESERTS", href="/deserts", id="page-14-link"),
                dbc.NavLink("SAUCES", href="/sauces", id="page-15-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

content = html.Div(

    id="page-content",
    style=CONTENT_STYLE)

app.layout = html.Div([
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)


@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 16)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 16)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P("After a fancy drink?")
    elif pathname == "/page-2":
        return html.P("Drinking with class tonight")
    elif pathname == "/page-3":
        return html.P("Out with the mates?")
    elif pathname == "/page-4":
        return html.P("Blending with the young crowd")
    elif pathname == "/page-5":
        return html.P("Good choice")
    elif pathname == "/page-6":
        return html.P("The shakes are amazing")
    elif pathname == "/page-7":
        return html.P("Great for a cold night")
    elif pathname == "/page-8":
        return html.P("Something to begin the meals")
    elif pathname == "/page-9":
        return html.P("It's time to feast!")
    elif pathname == "/page-10":
        return html.P("These are massive")
    elif pathname == "/page-11":
        return html.P("Lots of goods neatly wrapped")
    elif pathname == "/page-12":
        return html.P("Some extra bites")
    elif pathname == "/page-13":
        return html.P("There is somehing for everyone")
    elif pathname == "/page-14":
        return html.P("Close up dinner with a tasty treat!")
    elif pathname == "/page-15":
        return html.P("The most important part of any dish")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
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
        dbc.Button("MENU", outline=True, className="ms-4", id="btn_sidebar", color="light"),
        dbc.NavbarBrand("Eshaan's Kitchen", className="ms-3 card-title"),
        dbc.Button("TOTAL: $0.00", outline=True, className="ms-1 align-right", color="light"),
    ],
    color="danger",
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
                dbc.NavLink("DESSERTS", href="/desserts", id="page-14-link"),
                dbc.NavLink("SAUCES", href="/sauces", id="page-15-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

item1 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item1-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item1-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item1-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-2",
    id="item1-card",
)

item2 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item2-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item2-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item2-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-2",
    id="item2-card",
)

item3 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item3-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item3-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item3-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-2",
    id="item3-card",
)

item4 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item4-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item4-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item4-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-2",
    id="item4-card",
)

item5 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item5-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item5-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item5-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-2",
    id="item5-card",
)

item6 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="https://i1.sndcdn.com/avatars-000157669327-yxvhnx-original.png",
                        id="item2-image-ref",
                        width="140", height="140",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Wine", className="card-title", id="item6-title"),
                            html.P(
                                "Toasted ciabatta bread served hot with garlic butter.",
                                className="card-text", id="item6-desc",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Button("$10.00", outline=True, color="danger", id="item6-cost"),
                                    ),
                                ],
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex",
        )
    ],
    className="mb-3",
    id="item6-card",
)

content = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"), id="menu-category-desc")),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(item1),
                dbc.Col(item2),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(item3),
                dbc.Col(item4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(item5),
                dbc.Col(item6),
            ]
        ),
    ],
    id="page-content",
    style=CONTENT_STYLE)

modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Preview your food in Augmented Reality")),
                dbc.ModalBody(html.Video(
                    src="/videos/preview.mp4",
                    autoPlay=True,                        
                )),
                html.Hr(),
                dbc.ModalBody(html.Video(
                    src="/videos/preview.mp4",
                    autoPlay=True,                        
                )),
                html.Hr(),
                dbc.ModalBody(html.Video(
                    src="/videos/preview.mp4",
                    autoPlay=True,                        
                )),
                dbc.ModalFooter(
                    dbc.Button(
                        "Add to Cart", id="close", className="ms-auto", n_clicks=0, color="danger",
                    )
                ),
            ],
            id="modal",
            is_open=False,
            size="xl",
        ),
    ]
)

app.layout = html.Div([
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
        modal,
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

# The list content from lines 410 - 598 has been borrowed from the official TGI Friday online order portal
# as this is a prototype, the items, details and prices themselves are not critical to the design of this app

# Item titles, functions for updating and displaying
cocktails = ["Strawberry Daiquiri", "Long Island", "Electric Lemonade", "Pink Martini", "Mojito", "Margarita"]
wines = ["Prosecco", "Moscato", "Sauvignon blanc", "Chardonnay", "Rosé", "Merlot"]
beers = ["Pale Ale", "Great Northern", "Carlton Draught", "Pacific Ale", "Victoria Bitter", "Corona"]
spirits = ["Vodka", "London Dry Gin", "Sydney Dry Gin", "Bundaberg Rum", "Kraken", "Tequila"]
nonalcohol = ["Sprite", "Coke", "Fanta", "Solo", "Red Bull", "Pepsi"]
colddrinks = ["Vanilla Milkshake", "Chocolate Milkshake", "Strawberry Milkshake", "Pineapple Smoothie", "Grape Smoothie", "Apple Smoothie"]
hotdrinks = ["Hot Chocolate", "Cappuccino", "Flat White", "Latte", "Espresso", "Macchiato"]
starters = ["Chicken Wings", "Calamari", "Garlic Ciabatta", "Mac 'N' Cheese", "Mozzarella Sticks", "Chicken Strips"]
mains = ["Chicken Tenders", "Fish and Chips", "Glazed Chicken", "Glazed Salmon", "Prawn Fettuccine", "Meat Lovers Pizza"]
burgers = ["Bacon Cheeseburger", "Chicken Burger","Cajun Chicken Burger", "Texas Cowboy", "The Aussie", "Triple Stacker"]
wraps = ["Chicken Wrap", "Beef Wrap", "Pulled Pork Wrap", "Pork Wrap", "NA", "NA"]
sides = ["Seasonal Vegetables", "Mash Potato", "Thick Cut Fries", "Shortstring Fries", "Onion Rings", "Mac 'N' Cheese"]
kids = ["Cheese Pasta", "Tomato Napoli", "Mini Cheeseburger", "Chicken Nuggets", "Calamari", "Fish and Chips"]
desserts = ["Brownie", "Chocolate Sundae", "Sticky Date Pudding", "Raspberry Cheesecake", "Lemon Cheesecake", "Ice-cream"]
sauces = ["Tomato", "Smokey Barbeque", "Aioli", "Gravy", "Mayo", "Mustard"]
@app.callback([Output(f"item{i}-title", "children") for i in range(1, 7)], [Input("url", "pathname")])
def update_page_titles(pathname):
    if pathname in ["/", "/cocktails"]:
        return [html.P(cocktails[i]) for i in range(0, 6)]
    elif pathname == "/wine":
        return [html.P(wines[i]) for i in range(0, 6)]
    elif pathname == "/beer-and-cider":
        return [html.P(beers[i]) for i in range(0, 6)]
    elif pathname == "/spirits":
        return [html.P(spirits[i]) for i in range(0, 6)]
    elif pathname == "/non-alcoholic":
        return [html.P(nonalcohol[i]) for i in range(0, 6)]
    elif pathname == "/cold-drinks":
        return [html.P(colddrinks[i]) for i in range(0, 6)]
    elif pathname == "/hot-drinks":
        return [html.P(hotdrinks[i]) for i in range(0, 6)]
    elif pathname == "/starters":
        return [html.P(starters[i]) for i in range(0, 6)]
    elif pathname == "/mains":
        return [html.P(mains[i]) for i in range(0, 6)]
    elif pathname == "/burgers":
        return [html.P(burgers[i]) for i in range(0, 6)]
    elif pathname == "/wraps":
        return [html.P(wraps[i]) for i in range(0, 6)]
    elif pathname == "/sides":
        return [html.P(sides[i]) for i in range(0, 6)]
    elif pathname == "/kids-menu":
        return [html.P(kids[i]) for i in range(0, 6)]
    elif pathname == "/desserts":
        return [html.P(desserts[i]) for i in range(0, 6)]
    elif pathname == "/sauces":
        return [html.P(sauces[i]) for i in range(0, 6)]
    
# Item descriptions, functions for updating and displaying
Tcocktails = ["Pampero Blanco white rum, strawberry, lemon, lime and pure cane sugar. Served frozen with a sugared rim.", 
             "Smirnoff vodka, Pampero Blanco white rum, Greenall's gin, brandy, Marie Brizard triple sec, lemon, lime, pure cane sugar and Coca-Cola.", 
             "Smirnoff vodka, Marie Brizard Blue Curaçao, lemon, lime, pure cane sugar and lemonade, garnished with fresh lemon.", 
             "Smirnoff vodka, cranberry, pineapple and lime, poured table-side over pink fairy floss.", 
             "Pampero Blanco white rum, Paraiso lychee liqueur, lychee fruit, brown sugar, lime and mint, topped with soda.", 
             "El Jimador Reposado tequila, lemon, lime, pure cane sugar and passionfruit with a sea salt rim."]
Twines = ["Mornington Peninsula, VIC. Fresh and dry with aromas of citrus, apple and pear leading to a bright zesty finish.", 
          "Mornington Peninsula, VIC. Bright aromatics with pungent scents of tropical flowers. The palate is crisp, fresh and lush.", 
          "South East Aus", 
          "Yarra Valley, VIC. The wine is fresh, light and lively without being lean you'll find vibrance with just a dusting of spicy oak.", 
          "Heathcote, VIC. Beguiling red fruit aromas, savoury tannins and firm yet elegant structure.", 
          "South East Aus"]
Tbeers = ["NSW, 4.2%", 
          "QLD 3.5%", 
          "VIC 4.4%", 
          "VIC 4.4%", 
          "VIC 4.9%", 
          "VIC 4.5%"]
Tspirits = ["Smirnoff Red", 
            "Hayman", 
            "Hayman", 
            "Original", 
            "Black Spiced Rum", 
            "El Jimador Reposado"]
Tnonalcohol = ["600mL", 
               "600mL", 
               "600mL", 
               "600mL", 
               "600mL", 
               "600mL"]
Tcolddrinks = ["Vanilla ice cream, full cream milk and vanilla flavour, topped with whipped cream.", 
               "Vanilla ice cream, full cream milk and chocolate flavour, topped with whipped cream.", 
               "Vanilla ice cream, full cream milk and strawberry flavour, topped with whipped cream.", 
               "A mix of fruits blended together consisting mostly of pineapple", 
               "A mix of fruits blended together consisting mostly of grape", 
               "A mix of fruits blended together consisting mostly of apple"]
Thotdrinks = ["Served in a short mug", 
              "Served in a short glass", 
              "Served in a short mug", 
              "Served in a short glass", 
              "Served in a short mug", 
              "Served in a short glass"]
Tstarters = ["Select your choice of sauce: Smokey Chipotle & Honey (GF), Spicy Buffalo (GF), FRIDAYS™ Signature Whiskey Glaze, FRIDAYS™ Whiskey Glaze Blaze", 
             "Beautifully cooked calamari (6 pieces), served with a fresh gardan salad and two dipping sauces", 
             "Toasted ciabatta bread served hot with garlic butter", 
             "Golden and crunchy coating filled with creamy mac 'n' cheese, served with a side of roasted garlic aioli.", 
             "Crunchy breaded sticks of stringy melted mozzarella, served with ranch dipping sauce.", 
             "Tender chicken breast strips coated with crispy panko breadcrumbs, tossed in FRIDAYS™ Signature Whiskey Glaze made with Jack Daniel’s®"]
Tmains = ["Crispy golden chicken tenders, served with a side of fries, slaw and honey mustard dipping sauce", 
          "Battered hoki served with a side of shoestring fries, garden salad, tartare sauce and a lemon wedge.", 
          "Chicken breast char-grilled and basted with FRIDAYS™ Signature Whiskey Glaze made with Jack Daniel’s®, served with thick cut fries and garden salad", 
          "Flame-grilled salmon fillet basted with FRIDAYS™ Signature Whiskey Glaze made with Jack Daniel’s®, served with thick cut fries and garden salad", 
          "Cajun seasoned chicken breast and prawns, sautéed with red and green capsicum and onion, tossed through a creamy Cajun Alfredo fettuccine", 
          "An evenly cooked pizza on a sour dough base with lots of meats to satisfy the hungriest of appetites!"]
Tburgers = ["Grass-fed beef patty topped with melted American style cheese, peppered bacon, lettuce, tomato, red onion, pickles, ketchup, American mustard and roasted garlic", 
            "Crispy fried chicken breast topped with melted Mexican style cheese, peppered bacon, lettuce, tomato and roasted garlic aioli. Served with fries and dipping sauce.", 
            "Grilled chicken breast with Cajun seasoning, crispy bacon, melted Mexican style cheese, lettuce, tomato, pickled jalapeños and Cajun mayo. Served with fries & dipping sauce.", 
            "Grass-fed beef patty topped with slow-cooked Mexican beef in adobo sauce, melted American style cheese, peppered bacon, lettuce, tomato, red onion, pickles", 
            "Love BUDS plant-based burger patty with melted plant-based cheese, lettuce, tomato, red onion, pickles, ketchup, American mustard and veganaise", 
            "Three grass-fed beef patties basted with FRIDAYS™ Signature Whiskey Glaze made with Jack Daniel’s®, stacked high with melted American style cheese"]
Twraps = ["Toasted flour tortilla with your choice of grilled or crispy fried chicken breast, cos lettuce, cheese, tomato and honey mustard sauce.", 
          "Toasted flour tortilla with slow-cooked Mexican beef in adobo sauce, Mexican style cheese, quinoa, black beans, corn, shredded lettuce, pico de gallo, pickled jalapeños", 
          "Toasted flour tortilla with slow-cooked pulled pork in garlic sauce, cheese, quinoa, black beans, corn, shredded lettuce, pico de gallo, pickled jalapeños", 
          "Toasted flour tortilla with slow-cooked pork in BBQ sauce, American style cheese, quinoa, black beans, corn, shredded lettuce, pico de gallo, pickled jalapeños", 
          "-", 
          "-"]
Tsides = ["Cooked with garlic butter.", 
          "Vegan and Gluten Free", 
          "with Ketchup", 
          "with Ketchup", 
          "with Ranch", 
          "Vegan friendly"]
Tkids = ["Spaghetti served with a creamy cheese sauce", 
         "Spaghetti served with a rich tomato napoli sauce", 
         "Our signature burger only smaller", 
         "6 pieces", 
         "3 strips with salad", 
         "Carefully cooked fish served with a side of chips"]
Tdesserts = ["Chocolate brownie covered in hot chocolate fudge sauce, caramel sauce, creamy vanilla ice cream and chopped pecans.", 
             "Creamy vanilla ice cream topped with hot chocolate fudge sauce, caramel sauce, crushed OREO® and biscuit pieces and whipped cream with a cherry on top.", 
             "A tasty sticky date served with Ice-cream and a chocolate sauce", 
             "Divine raspberry cheesecake with a rich strawberry sauce", 
             "Divine lemon cheesecake with a cookie base", 
             "Two scoops of ice-cream with your choice of sauce"]
Tsauces = ["Served in a ramekin", 
           "Served in a ramekin", 
           "Served in a ramekin", 
           "Served in a ramekin", 
           "Served in a ramekin", 
           "Served in a ramekin"]
@app.callback([Output(f"item{i}-desc", "children") for i in range(1, 7)], [Input("url", "pathname")])
def update_page_titles(pathname):
    if pathname in ["/", "/cocktails"]:
        return [html.P(Tcocktails[i]) for i in range(0, 6)]
    elif pathname == "/wine":
        return [html.P(Twines[i]) for i in range(0, 6)]
    elif pathname == "/beer-and-cider":
        return [html.P(Tbeers[i]) for i in range(0, 6)]
    elif pathname == "/spirits":
        return [html.P(Tspirits[i]) for i in range(0, 6)]
    elif pathname == "/non-alcoholic":
        return [html.P(Tnonalcohol[i]) for i in range(0, 6)]
    elif pathname == "/cold-drinks":
        return [html.P(Tcolddrinks[i]) for i in range(0, 6)]
    elif pathname == "/hot-drinks":
        return [html.P(Thotdrinks[i]) for i in range(0, 6)]
    elif pathname == "/starters":
        return [html.P(Tstarters[i]) for i in range(0, 6)]
    elif pathname == "/mains":
        return [html.P(Tmains[i]) for i in range(0, 6)]
    elif pathname == "/burgers":
        return [html.P(Tburgers[i]) for i in range(0, 6)]
    elif pathname == "/wraps":
        return [html.P(Twraps[i]) for i in range(0, 6)]
    elif pathname == "/sides":
        return [html.P(Tsides[i]) for i in range(0, 6)]
    elif pathname == "/kids-menu":
        return [html.P(Tkids[i]) for i in range(0, 6)]
    elif pathname == "/desserts":
        return [html.P(Tdesserts[i]) for i in range(0, 6)]
    elif pathname == "/sauces":
        return [html.P(Tsauces[i]) for i in range(0, 6)]

# Item prices, functions for updating and displaying
Pcocktails = ["$23.90", "$23.90", "$23.90", "$17.90", "$16.90", "$18.90"]
Pwines = ["$14.90", "$14.90", "$16.90", "$16.90", "$12.90", "$12.90"]
Pbeers = ["$8.90", "$8.90", "$7.90", "$7.90", "$9.90", "$6.90"]
Pspirits = ["$9.90", "$12.90", "$12.90", "$12.90", "$9.90", "$9.90"]
Pnonalcohol = ["$4.90", "$4.90", "$4.90", "$4.90", "$4.90", "$4.90"]
Pcolddrinks = ["$7.50", "$7.50", "$7.50", "$12.50", "$12.50", "$12.50"]
Photdrinks = ["$5.90", "$4.90", "$4.90", "$7.90", "$6.90", "$5.90"]
Pstarters = ["$18.00", "$16.00", "$12.00", "$14.00", "$10.00", "$15.00"]
Pmains = ["$24.90", "$22.90", "$26.50", "$27.50", "$22.50", "$21.90"]
Pburgers = ["$18.90", "$17.90","$18.90", "$21.90", "$20.90", "$22.90"]
Pwraps = ["$21.90", "$22.90", "$22.90", "$21.90", "-", "-"]
Psides = ["$10.00", "$9.90", "$13.00", "$12.00", "$8.90", "$12.90"]
Pkids = ["$14.90", "$14.90", "$12.50", "$16.00", "!0.50", "$14.90"]
Pdesserts = ["$8.20", "$12.50", "$9.80", "$10.90", "411.00", "$5.00"]
Psauces = ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"]
@app.callback([Output(f"item{i}-cost", "children") for i in range(1, 7)], [Input("url", "pathname")])
def update_page_titles(pathname):
    if pathname in ["/", "/cocktails"]:
        return [html.P(Pcocktails[i]) for i in range(0, 6)]
    elif pathname == "/wine":
        return [html.P(Pwines[i]) for i in range(0, 6)]
    elif pathname == "/beer-and-cider":
        return [html.P(Pbeers[i]) for i in range(0, 6)]
    elif pathname == "/spirits":
        return [html.P(Pspirits[i]) for i in range(0, 6)]
    elif pathname == "/non-alcoholic":
        return [html.P(Pnonalcohol[i]) for i in range(0, 6)]
    elif pathname == "/cold-drinks":
        return [html.P(Pcolddrinks[i]) for i in range(0, 6)]
    elif pathname == "/hot-drinks":
        return [html.P(Photdrinks[i]) for i in range(0, 6)]
    elif pathname == "/starters":
        return [html.P(Pstarters[i]) for i in range(0, 6)]
    elif pathname == "/mains":
        return [html.P(Pmains[i]) for i in range(0, 6)]
    elif pathname == "/burgers":
        return [html.P(Pburgers[i]) for i in range(0, 6)]
    elif pathname == "/wraps":
        return [html.P(Pwraps[i]) for i in range(0, 6)]
    elif pathname == "/sides":
        return [html.P(Psides[i]) for i in range(0, 6)]
    elif pathname == "/kids-menu":
        return [html.P(Pkids[i]) for i in range(0, 6)]
    elif pathname == "/desserts":
        return [html.P(Pdesserts[i]) for i in range(0, 6)]
    elif pathname == "/sauces":
        return [html.P(Psauces[i]) for i in range(0, 6)]
    
@app.callback(Output("menu-category-desc", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/cocktails"]:
        return html.H4("COCKTAILS")
    elif pathname == "/wine":
        return html.H4("WINE")
    elif pathname == "/beer-and-cider":
        return html.H4("BEER & CIDER")
    elif pathname == "/spirits":
        return html.H4("SPIRITS")
    elif pathname == "/non-alcoholic":
        return html.H4("NON-ALCOHOLIC")
    elif pathname == "/cold-drinks":
        return html.H4("COLD DRINKS")
    elif pathname == "/hot-drinks":
        return html.H4("HOT DRINKS")
    elif pathname == "/starters":
        return html.H4("STARTERS")
    elif pathname == "/mains":
        return html.H4("MAINS")
    elif pathname == "/burgers":
        return html.H4("BURGERS")
    elif pathname == "/wraps":
        return html.H4("WRAPS")
    elif pathname == "/sides":
        return html.H4("SIDES")
    elif pathname == "/kids-menu":
        return html.H4("KIDS MENU")
    elif pathname == "/desserts":
        return html.H4("DESSERTS")
    elif pathname == "/sauces":
        return html.H4("SAUCES")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Add a popup window after clicking on button 6, id="item{i}-cost"
@app.callback(
    Output("modal", "is_open"),
    [Input("item6-cost", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server()
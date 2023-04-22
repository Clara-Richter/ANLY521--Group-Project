import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from Code.entities import extract_entities

import spacy
import dash_bootstrap_components as dbc

available_packages = ['en_ner_bionlp13cg_md',]


nlp = spacy.load('en_ner_bionlp13cg_md')

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


### Navbar ###

# add more NavItem - NavLink to add link to new pages in the Navbar
nav_contents = [
                dbc.NavItem(dbc.NavLink("About Us", href="/about-us",
                                        className="px-3 text-light")),
                dbc.NavItem(dbc.NavLink("Medical-text Translation", href="/our-work",
                                        className="px-3 text-light")),
                dbc.NavItem(dbc.NavLink("Our Python Package", href="/our-work",
                                        className="px-3 text-light")),
                dbc.NavItem(dbc.NavLink("References", href="#",
                                        className="px-3 text-light")),
]


nav1 = dbc.Nav(nav_contents, pills=True, fill=True)


navbar = dbc.NavbarSimple(
    children=[nav1],
    brand="Easy Medical Documents using NLP",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
    className='fixed-top'
)

# Control section giving options
controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Select Language"),
                dcc.Dropdown(
                    id="language-selection",
                    options=['1', '2', '3'],
                    value='what_is value'   # "value" sets the default value
                )
            ]
        ),

        html.Br(),

        html.Div(
            [
                dbc.Label("Select spaCy Model"),
                dcc.Dropdown(
                    id="model-selection",
                    options=['1', '2', '3'],
                    value='what_is value'   # "value" sets the default value
                )
            ]
        )
    ],
    body=True,
    color="light"
)


# define the home page layout
home_layout = dbc.Container(
    [
        html.H1("Welcome to our app!"),
        html.P("This is the home page."),
    ],
    style={"padding-top": "5rem"}  # add padding to push the content down so that the Navbar doesn't cover the content
)


# define the about us page layout
about_us_layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardImg(src="/assets/img/team-member-1.jpg", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Clara Richter", className="card-title"),
                                html.P(
                                    ["M.S. in Data Science",
                                     html.Br(),
                                     "Georgetown University"],
                                    className="card-text"),
                            ]
                        )
                    ]
                )
            ],
        md=4
        ),

        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardImg(src="./img/HyuksooShin_hs1062.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Hyuksoo Shin", className="card-title"),
                                html.P(
                                    ["M.S. in Data Science",
                                     html.Br(),
                                     "Georgetown University"],
                                    className="card-text"),
                            ]
                        )
                    ]
                )
            ],
        md=4
        ),

        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardImg(src="/assets/img/team-member-1.jpg", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Ryan Walter", className="card-title"),
                                html.P(
                                    ["M.S. in Data Science",
                                     html.Br(),
                                     "Georgetown University"],
                                    className="card-text"),
                            ]
                        )
                    ]
                )
            ],
        md=4
        ),
    ],
    style = {"padding-top": "5rem"}  # add padding to push the content down so that the Navbar doesn't cover the content
    )
])


# Main body
ourwork_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    controls,
                    md=4,
                    style={"height": "100%", "box-sizing": "border-box"}
                ),
                dbc.Col(
                    [
                        dcc.Textarea(
                            id='input-text',
                            placeholder='Enter text here...',
                            style={
                                'width': '100%',
                                'height': '300px',
                                'box-sizing': 'border-box'
                            },
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Button("Summarization",
                                               id="summarize-button",
                                               color="success"),
                                    className="d-grid gap-2"
                                ),

                                dbc.Col(
                                    dbc.Button("NER", id="ner-button", color="warning"),
                                    className="d-grid gap-2"
                                )
                            ],
                            justify="center",
                            className="mt-3 text-center justify-content_center"
                        )

                    ],
                    md=8,
                    style={"height": "100%", "box-sizing": "border-box"}
                ),
            ],
            align="stretch",
        )
    ],
    style={"padding-top": "5rem"}   # add padding to push the content down so that the Navbar doesn't cover the content

)


# define the app layout
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div(id="page-content")
])


# define the callback function to switch between pages based on URL path
@app.callback(Output("page-content", "children"),
              Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/about-us":
        return about_us_layout
    elif pathname == "/our-work":
        return ourwork_layout
    else:
        return home_layout


#     html.Div([
#     html.H1(
#         children = "Using NLP to Better Understand Medical Documents",
#         style={'textAlign': 'center'}
#     ),
#
#     html.Div(children='Your medical documents can be summarized here!',
#              style={'textAlign': 'center'}),
#
#     html.Br(),
#
#     html.Div(children=[
#         html.Label('Select spaCy Model'),
#         dcc.Dropdown(['en_ner_bionlp13cg_md', 'en_ner_bc5cdr_md'],
#                      style={'width': '80%'}),
#     ]),
#
#     html.Br(),
#
#     dcc.Textarea(
#         id='input-text',
#         placeholder='Enter text here...',
#         style={'width': '80%', 'height': '200px'}
#     ),
#     html.Button('Submit', id='submit-button', n_clicks=0),
#     html.Div(id='output')
# ])

@app.callback(Output('output', 'children'),
              Input('submit-button', 'n_clicks'),
              State('input-text', 'value'))
def update_output(n_clicks, input_text):
    if n_clicks is not None and n_clicks > 0:
        output_list = extract_entities(input_text)
        return html.Ul([
            html.Li(f"{text} ({label}") for text, label in output_list
        ])

    return "Please enter text"


if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from Code.entities import extract_entities
from Code.utils.display import display_entities
from Code.summarization import SumText

import spacy
import dash_bootstrap_components as dbc

available_packages = ['en_ner_bionlp13cg_md', 'en_ner_bc5cdr_md', 'en_core_web_sm']


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
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

# # Control section giving options
# controls = dbc.Card(
#     [
#
#         html.Div(
#             [
#                 dbc.Label("Select spaCy Model"),
#                 dcc.Dropdown(
#                     id="model-selection",
#                     options=available_packages,
#                     value='en_ner_bc5cdr_md'   # "value" sets the default value
#                 )
#             ]
#         )
#     ],
#     body=True,
#     color="light"
# )


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
                        dbc.CardImg(src="img/HyuksooShin_hs1062.png", top=True),
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
                # dbc.Col(
                #     controls,
                #     md=4,
                #     style={"height": "100%", "box-sizing": "border-box"}
                # ),
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
                                               color="success",
                                               n_clicks=0),
                                    className="d-grid gap-2"
                                ),

                                dbc.Col(
                                    dbc.Button("Add Definitions",
                                               id="definitions-button",
                                               color="secondary",
                                               n_clicks=0),
                                    className="d-grid gap-2"
                                ),

                                dbc.Col(
                                    dbc.Button("Entities", id="entities-button", color="warning",
                                               n_clicks=0),
                                    className="d-grid gap-2"
                                ),

                                dbc.Col(
                                    dbc.Button("Display NER",
                                               id="display-button",
                                               color="primary",
                                               n_clicks=0),
                                    className="d-grid gap-2"
                                ),
                            ],
                            justify="center",
                            className="mt-3 text-center justify-content_center"
                        )

                    ],
                    md=12,
                    style={"height": "100%", "box-sizing": "border-box"}
                ),
            ],
            align="stretch",
        ),

        html.Br(),
        html.Br(),
        html.H4("Output Section",
                className="p-3 mb-2 bg-secondary text-white border"),
        html.Div(id="output")
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


@app.callback(Output('output', 'children', allow_duplicate=True),
              Input('summarize-button', 'n_clicks'),
              State('input-text', 'value'),
              prevent_initial_call=True
              )
def update_summarize_output(n_clicks, input_text):
    if n_clicks is not None and n_clicks > 0 and input_text:
        s = SumText(input_text)
        res = s.summarize()
        return [html.P("Summarization:"), html.P(res)]
    return "Please enter text"


@app.callback(Output('output', 'children', allow_duplicate=True),
              Input('entities-button', 'n_clicks'),
              State('input-text', 'value'),
              prevent_initial_call=True
              )
def update_entities_output(n_clicks, input_text):
    if n_clicks is not None and n_clicks > 0 and input_text:
        output_list = extract_entities(input_text)
        return [
            html.P("Entities:"),
            html.Ul([html.Li(f"{text} ({label})") for text, label in output_list])
        ]
    return "Please enter text"


@app.callback(Output('output', 'children', allow_duplicate=True),
              Input('definitions-button', 'n_clicks'),
              State('input-text', 'value'),
              prevent_initial_call=True
              )
def update_definitions_output(n_clicks, input_text):
    if n_clicks is not None and n_clicks > 0 and input_text:
        s = SumText(input_text)
        res = s.add_definitions()
        return [html.P("Add definitions:"), html.P(res)]
    return "Please enter text"


@app.callback(Output('output', 'children', allow_duplicate=True),
              #Input('model-selection', 'value'),
              Input('display-button', 'n_clicks'),
              State('input-text', 'value'),
              prevent_initial_call=True
              )
def update_display_output(n_clicks, input_text):
    if n_clicks is not None and n_clicks > 0 and input_text:
        html_entities = display_entities(input_text)
        return [html.P("Display NER:"), dcc.Markdown([html_entities], dangerously_allow_html=True)]
    return "Please enter text"


if __name__ == '__main__':
    app.run_server(debug=True)
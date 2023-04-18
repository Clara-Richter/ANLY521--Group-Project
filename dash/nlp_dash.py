import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from Code.entities import extract_entities
import spacy

nlp = spacy.load('en_ner_bionlp13cg_md')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        children = "Using NLP to Better Understand Medical Documents",
        style={'textAlign': 'center'}
    ),

    html.Div(children='Your medical documents can be summarized here!',
             style={'textAlign': 'center'}),

    html.Br(),

    html.Div(children=[
        html.Label('Select spaCy Model'),
        dcc.Dropdown(['en_ner_bionlp13cg_md', 'en_ner_bc5cdr_md'],
                     style={'width': '80%'}),
    ]),

    html.Br(),

    dcc.Textarea(
        id='input-text',
        placeholder='Enter text here...',
        style={'width': '80%', 'height': '200px'}
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output')
])

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
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#initalise the app
app=Dash(__name__)

#allow for hosting on render.
server=app.server

colors={
    'background':'#111111',
    'text':'#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Campus": ["UON", "TUK", "Daystar Uni", "JKUAT", "KU", "KCA"],
    "Admissions": [4000, 1800, 2500, 8000, 4500, 3500],
    "County": ["Nairobi", "Nairobi", "Nairobi", "Kiambu", "Kiambu", "Kiambu"]
})

fig = px.bar(df, x="Campus", y="Admissions", color="County", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundcolor':colors['background']} ,children=[
    html.H1(children='University Campuses',style={'textAlign':'center','color':colors['text']}),

    html.Div(children='Admissions per campus for the year 2023.', style={'textAlign':'center','color':colors['text']}),

    dcc.Graph(figure=fig,id='barGraph')
])

if __name__ == '__main__':
    app.run(debug=True,port=5050)

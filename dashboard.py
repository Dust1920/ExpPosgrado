from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)

app.title = "Comparativa"


app.layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[
            html.H1("Comparando Tarjetas de Crédito")
        ]),
    ], className="header"),
        html.Div(children=[
            html.H1("Tarjetas de Crédito", className="cards-menu"),
            dcc.Tabs(children=[
                dcc.Tab(label = "Tarjeta 1", children=[
                html.Div(children=[
                    html.Div(children=[
                        html.H2("Cobros"),
                        html.H3("Gasto Minimo Mensual: $3000.00")
                    ], className="c1"),
                    html.Div(children=[
                        html.H2("Beneficio"),
                        html.H3("Cashback"),
                        html.H4("General: 2%"),
                        html.H4("Categoria 1: 0%"),
                        html.H4("Categoria 2: 0%"),
                        html.H4("Categoria 3: 0%"),
                    ], className="c2")
            ], className="multicolumn"),
                ], className="card-1", selected_className="acard-1"),
                dcc.Tab(label = "Tarjeta 2", children=[
                html.Div(children=[
                    html.Div(children=[
                        html.H2("Cobros"),
                        html.H3("Gasto Minimo Mensual: $300.00")
                    ], className="c1"),
                    html.Div(children=[
                        html.H2("Beneficio"),
                        html.H3("Cashback"),
                        html.H4("General: 0'%"),
                        html.H4("Categoria 1: 4%"),
                        html.H4("Categoria 2: 5%"),
                        html.H4("Categoria 3: 6%"),
                    ], className="c2")
            ], className="multicolumn"),
                ], className="card-2", selected_className="acard-2")
            ])
        ], className="cards")
])






if __name__ == "__main__":
    app.run_server(debug = True)
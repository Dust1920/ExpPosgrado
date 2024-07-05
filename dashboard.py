from dash import Dash, Input, Output, dcc, html
import cashback_model as model
import plotly.express as px

app = Dash(__name__)
app.title = "Comparando Tarjetas de Crédito"

app.layout = html.Div(
    html.Div(children=[
        html.Div(children=[
            html.H1("Seleccione su tarjeta"),
            dcc.Dropdown(id = "cards", options = ["Tarjeta 1", "Tarjeta 2", "Tarjeta 3"], value = "Tarjeta 1",
                         clearable=False, style={"margin":"10px"}),
            html.H1("Defina el Limite de Crédito"),
            dcc.Input(id = "limit", type = "number", debounce= True, value = 20_000, style={"font-size":"30px"}),
            html.H1("Información del Cashback"),
            html.Div(id = "card-data")
        ],style={"width":"50%"}),
        html.Div(children=[
            html.H1("Registro Compras / Cashback"),
            dcc.Dropdown(id = "plot-mode", options = ["Compras","Cashback"], value = "Compras", clearable=False, style={"margin":"10px"}),
            dcc.Graph(id = "card-cashback")
        ],style={"width":"50%"}),
    ], className="multicolumn")
)








@app.callback(
    Output("card-cashback","figure"), Input("plot-mode","value"), Input("cards","value"), Input("limit","value")
)

def plot_cashback(mode, card, limit):
    Tarjeta_1 = {
        "Nombre": "Tarjeta 1",
        "Cashback": {
            "Porcentaje": [0.02],
            "Probabilidad": [1]
        } 
    }
    Tarjeta_2 = {
        "Nombre": "Tarjeta 2",
        "Cashback": {
            "Porcentaje": [0, 0.04, 0.05, 0.06],
            "Probabilidad": [0.7, 0.1 ,0.1 , 0.1]
        } 
    }

    Tarjeta_3 = {
        "Nombre": "Tarjeta 3",
        "Cashback": {
            "Porcentaje": [0.005, 0.05, 0.05, 0.05],
            "Probabilidad": [0.85, 0.05 ,0.05 , 0.05]
        } 
    }
    fig = px.pie(names = ["a"], values=[0])
    compras = [0]
    comcash = [0]
    if mode:
        if card == "Tarjeta 1":
            compras, comcash = model.simul_creditcard(limit, Tarjeta_1)
        if card == "Tarjeta 2":
            compras, comcash = model.simul_creditcard(limit, Tarjeta_2)
        if card == "Tarjeta 3":
            compras, comcash = model.simul_creditcard(limit, Tarjeta_3)
        if mode == "Compras":
            fig = px.line(x = range(1,len(compras) + 1), y = compras)
        else:
            fig = px.line(x = range(1,len(comcash) + 1), y = comcash)
    return fig

@app.callback(
    Output("card-data","children"), Input("plot-mode","value"), Input("cards","value"), Input("limit","value")
)

def cashback_mean(mode, card, limit):
    Tarjeta_1 = {
        "Nombre": "Tarjeta 1",
        "Cashback": {
            "Porcentaje": [0.02],
            "Probabilidad": [1]
        } 
    }
    Tarjeta_2 = {
        "Nombre": "Tarjeta 2",
        "Cashback": {
            "Porcentaje": [0, 0.04, 0.05, 0.06],
            "Probabilidad": [0.7, 0.1 ,0.1 , 0.1]
        } 
    }

    Tarjeta_3 = {
        "Nombre": "Tarjeta 3",
        "Cashback": {
            "Porcentaje": [0.005, 0.05, 0.05, 0.05],
            "Probabilidad": [0.85, 0.05 ,0.05 , 0.05]
        } 
    }
    cb_m = 0 
    if mode:
        if card == "Tarjeta 1":
            cb_m = model.cb_mean(limit, Tarjeta_1)
        if card == "Tarjeta 2":
            cb_m = model.cb_mean(limit, Tarjeta_2)
        if card == "Tarjeta 3":
            cb_m = model.cb_mean(limit, Tarjeta_3)
    text = f"Con una muestra de {model.N_SIMUL} simulaciones, la tarjeta genera un cashback promedio de {round(cb_m, 2)}%"
    return text






if __name__ == "__main__":
    app.run_server(debug = True)



"""
    Expositions
"""
import pandas as pd

transactions = pd.read_excel("Expenses.xlsx")

YEARS = list(transactions['Year'].unique())
MONTHS = list(transactions['Month'].unique())

# print(MONTHS)


m0 = MONTHS[0]
y0 = YEARS[1]

# Expenses
expenses = transactions[transactions['Amount'] > 0]

def prop_s(moo):
    """
    Calc History
    """
    exp_y = expenses[expenses['Year'] == y0]
    exp_ym = exp_y[exp_y['Month'] == moo]
    # print(exp_ym.shape)
    # exp_ym = exp_y.copy()

    # Transactions
    trans_y = transactions[transactions['Year'] == y0]
    trans_ym = trans_y[trans_y['Month'] == moo]
    if len(exp_ym) == 0:
        return 0

    # HSBC 2Now
    cb_2now = exp_ym['Amount'].sum() * 0.02

    # Santander Like U
    ## Farmacias
    exp_phar = exp_ym[exp_ym['SubCategory'] == "Pharmacy"]
    ph_s = exp_phar['Amount'].sum() * 0.06

    ## Entretenimiento y Restaurantes
    exp_ent = exp_ym[exp_ym['Category'] == "Entertainment"]
    ph_ent = exp_ent['Amount'].sum() * 0.05

    exp_res = exp_ym[exp_ym['SubCategory'] == "Restaurant"]
    ph_res = exp_res['Amount'].sum() * 0.05

    ## Gasolina
    exp_gas = exp_ym[exp_ym['SubCategory'] == "Gas"]
    ph_gas = exp_gas['Amount'].sum() * 0.04


    # Citibanamex Oro
    ## Gasolina
    oro_gas = exp_gas['Amount'].sum() * 0.14 * 0.1

    ## General
    oro_gen = exp_ym['Amount'].sum() * 0.07 * 0.1
    # print(oro_gen)



    # BBVA Oro


    bbva_p = trans_ym[trans_ym['Category'] == "Bank"]
    bbva_pc = bbva_p[bbva_p['SubCategory'] == "Points"]
    cash_bbva = -1.0 * bbva_pc['Amount'].sum()

    cash_perc = cash_bbva / exp_ym['Amount'].sum()

    cashback = {
        "H2Now": cb_2now,
        "LikeU": ph_s + ph_ent + ph_res + ph_gas,
        "BBVA_ORO": cash_bbva,
        "CITI_ORO": oro_gas + oro_gen
    }

    # Estimacion


    m_phar = exp_phar['Amount'].sum() if len(exp_phar) > 0 else 0
    # print(m_phar)

    m_gas = exp_gas['Amount'].sum() if len(exp_gas) > 0 else 0
    # print(m_gas)

    m_res = exp_res['Amount'].sum() if len(exp_res) > 0 else 0
    # print(m_res)

    m_ent = exp_ent['Amount'].sum() if len(exp_ent) > 0 else 0
    # print(m_ent)

    props = {
        "Farmacia":len(exp_phar) / len(expenses),
        "Rest y Ent":(len(exp_ent) + len(exp_res))/ len(expenses),
        "Gasolina":len(exp_gas) / len(expenses)
    }

    # print(props)

    gan_p = {
        "Farmacia": m_phar / exp_ym['Amount'].sum(),
        "Rest y Ent":(m_ent + m_res)/ exp_ym['Amount'].sum(),
        "Gasolina": m_gas / exp_ym['Amount'].sum()
    }

    S = 0
    v = [0.06, 0.05, 0.04]
    for t, x in enumerate(gan_p.keys()):
        S += v[t] * gan_p[x]
    return S

for m in MONTHS:
    print(m, prop_s(m))

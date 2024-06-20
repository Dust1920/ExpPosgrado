class CreditCard:
    def __init__(self, **kwargs) -> None:
        limit = kwargs.get("credit_limit", 0)
        cashback = kwargs.get("cashback", {0: 0})
        comissions = kwargs.get("costs", None)
        min_cost = kwargs.get("gasto_minimo", 0)
        self.credit_limit = limit
        self.cashback = cashback
        self.commisions = comissions
        self.min_cost = min_cost
    def get_cash():
        return 0


# HSBC 2Now
cashback_1 = {
    0: 2,
    1: 0,
    2: 0,
    3: 0
}


# Santander Like U
cashback_2 = {
    0: 2,
    1: 4,
    2: 5,
    3: 6
}



card1 = CreditCard(credit_limit = 100_000, gasto_minimo = 3000)

card2 = CreditCard(credit_limit = 80_000, gasto_minimo = 400)


print(card1.credit_limit)
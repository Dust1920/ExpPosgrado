"""
    Define the Credit Card Class
"""


class Creditcard:
    """
        Create Credit Cards
    """

    def __init__(self, credit_limit: int, grace_time: int):
        """
            Constructor of Credit Card
        """
        self.credit_limit = credit_limit
        self.grace_time = grace_time
        self.cut_period = 30
        self.msi = None
        self.cashback = None
        self.points = None
        self.transactions = None

    def select_benefits(self, **kwargs):
        """
            Select Benefits by Credit Card
        """
        cashback = kwargs.get("Cashback", [0, None])
        msi = kwargs.get("MSI", [0, None])
        points = kwargs.get("Points", [0, None])
        self.cashback = cashback
        self.msi = msi
        self.points = points

    def add_transactions(self, df):
        """
            Consider Transactions  
        """
        self.transactions = df

    def calc_cashback(self):
        """
        Given Transactions Calculate 
        """
        data = self.transactions
        cb = 0
        return cb

    def calc_msi(self):
        """
            Calc the Benefits of the Benefits
        """
        data = self.transactions
        ms = 0
        return ms

    def calc_points(self):
        """
        Calc the Benefits in Points
        """
        data = self.transactions
        p = 0
        return p

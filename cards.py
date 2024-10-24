"""
    Simulate Benefits in Credit Cards
"""
from creditcard import Creditcard


H2NOW = Creditcard(credit_limit=100_000, grace_time=20)
LikeU = Creditcard(credit_limit=100_000, grace_time=20)
BPlatinum = Creditcard(credit_limit=100_000, grace_time=20)
SClassic = Creditcard(credit_limit=100_000, grace_time=20)
SSimply = Creditcard(credit_limit=100_000, grace_time=20)

# HSBC 2Now
H2NOW.select_benefits(cashback = [1, {"General": 0.02}])

# Santander Like U
cb  = {"Gas":0.04, "Entertainment": 0.05, "Pharmacy": 0.06}
LikeU.select_benefits(cashback = [1, cb])

# BBVA Platinum
platinum_b = {"Ppoints": 23, "PointstoCashback":[[0.2, 0.1], [0.8, 0.07]]}
BPlatinum.select_benefits(points = [1, platinum_b])

# Banamex Simplicity
simply_b = {"Ppoints"}

# Banamex Clasica
classic_b = {"Ppoints"}

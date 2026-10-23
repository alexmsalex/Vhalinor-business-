def compound_growth(principal: float, annual_rate: float, years: int) -> float:
    if principal < 0 or years < 0 or annual_rate <= -1:
        raise ValueError("Parâmetros inválidos.")
    return principal * (1 + annual_rate) ** years

def monthly_contributions(principal: float, monthly_payment: float, annual_rate: float, years: int) -> float:
    if principal < 0 or monthly_payment < 0 or years < 0 or annual_rate <= -1:
        raise ValueError("Parâmetros inválidos.")
    months = years * 12
    r = (1 + annual_rate) ** (1 / 12) - 1
    base = principal * (1 + r) ** months
    deposits = monthly_payment * months if r == 0 else monthly_payment * (((1 + r) ** months - 1) / r)
    return base + deposits

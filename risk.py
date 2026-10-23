import numpy as np
import pandas as pd

def risk_summary(close: pd.Series) -> dict:
    prices = pd.to_numeric(close, errors="coerce").dropna()
    returns = prices.pct_change().dropna()
    vol = float(returns.std() * np.sqrt(252) * 100) if len(returns) > 1 else 0.0
    drawdown = prices / prices.cummax() - 1
    max_dd = float(drawdown.min() * 100) if len(drawdown) else 0.0
    period_return = float((prices.iloc[-1] / prices.iloc[0] - 1) * 100) if len(prices) > 1 and prices.iloc[0] else 0.0
    return {"annualized_volatility": vol, "max_drawdown": max_dd, "period_return": period_return}

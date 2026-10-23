import pandas as pd

def technical_snapshot(df: pd.DataFrame) -> dict:
    close = pd.to_numeric(df["Close"], errors="coerce").dropna()
    if len(close) < 15:
        return {"rsi": float("nan"), "interpretation": "Histórico insuficiente."}
    delta = close.diff()
    gains = delta.clip(lower=0).rolling(14).mean()
    losses = -delta.clip(upper=0).rolling(14).mean()
    rs = gains / losses.replace(0, float("nan"))
    rsi = 100 - 100 / (1 + rs)
    last_rsi = float(rsi.iloc[-1]) if pd.notna(rsi.iloc[-1]) else float("nan")
    sma20, sma50 = close.rolling(20).mean().iloc[-1], close.rolling(50).mean().iloc[-1]
    if pd.notna(last_rsi) and last_rsi < 30:
        interpretation = "RSI abaixo de 30: região tradicionalmente sobrevendida; não é sinal isolado de compra."
    elif pd.notna(last_rsi) and last_rsi > 70:
        interpretation = "RSI acima de 70: região tradicionalmente sobrecomprada; não é sinal isolado de venda."
    elif pd.notna(sma50) and close.iloc[-1] > sma20 > sma50:
        interpretation = "Preço acima das médias de 20 e 50 períodos; tendência recente positiva, sujeita a reversões."
    elif pd.notna(sma50) and close.iloc[-1] < sma20 < sma50:
        interpretation = "Preço abaixo das médias de 20 e 50 períodos; tendência recente negativa, sujeita a reversões."
    else:
        interpretation = "Sinais mistos/neutros; exija confirmação e controle de risco."
    return {"rsi": last_rsi, "interpretation": interpretation}

def moving_average_backtest(df: pd.DataFrame) -> dict:
    close = pd.to_numeric(df["Close"], errors="coerce").dropna()
    if len(close) < 55:
        return {}
    fast, slow = close.rolling(20).mean(), close.rolling(50).mean()
    signal = (fast > slow).astype(float).shift(1).fillna(0)
    returns = close.pct_change().fillna(0)
    strategy = signal * returns
    trades = int((signal.diff().abs().fillna(0) > 0).sum())
    strategy_return = ((1 + strategy).prod() - 1) * 100
    buy_hold = ((close.iloc[-1] / close.iloc[0]) - 1) * 100
    return {"strategy_return": float(strategy_return), "buy_hold_return": float(buy_hold), "trades": trades}

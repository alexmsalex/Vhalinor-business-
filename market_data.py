import pandas as pd
import yfinance as yf

def presets():
    return {
        "Ações Brasil": ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BOVA11.SA", "^BVSP"],
        "Ações EUA / ETFs": ["AAPL", "MSFT", "NVDA", "SPY", "QQQ"],
        "Criptoativos": ["BTC-USD", "ETH-USD", "SOL-USD"],
    }

def load_market_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    try:
        df = yf.download(ticker, period=period, auto_adjust=True, progress=False, threads=False)
        if df is None or df.empty:
            return pd.DataFrame()
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.rename_axis("Date").dropna(subset=["Close"])
        df["SMA20"] = df["Close"].rolling(20).mean()
        df["SMA50"] = df["Close"].rolling(50).mean()
        return df
    except Exception:
        return pd.DataFrame()

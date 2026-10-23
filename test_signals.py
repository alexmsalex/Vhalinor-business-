import pandas as pd
from src.signals import technical_snapshot, moving_average_backtest

def test_short_history_is_handled():
    df = pd.DataFrame({"Close": [10, 11, 12]})
    assert "insuficiente" in technical_snapshot(df)["interpretation"].lower()

def test_backtest_needs_enough_history():
    df = pd.DataFrame({"Close": range(1, 30)})
    assert moving_average_backtest(df) == {}

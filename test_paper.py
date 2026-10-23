import tempfile
from pathlib import Path
import src.paper as paper

def test_paper_order_is_recorded_and_never_needs_external_api(tmp_path, monkeypatch):
    monkeypatch.setattr(paper, "DB_PATH", tmp_path / "orders.sqlite3")
    broker = paper.PaperBroker()
    order = broker.submit("btc-usd", "buy", 0.01, 65000)
    assert order["ticker"] == "BTC-USD"
    assert order["notional"] == 650
    assert broker.recent_orders()[0]["side"] == "BUY"

def test_invalid_paper_order_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(paper, "DB_PATH", tmp_path / "orders.sqlite3")
    try:
        paper.PaperBroker().submit("AAPL", "BUY", 0, 100)
    except ValueError:
        return
    assert False, "Esperava ValueError"

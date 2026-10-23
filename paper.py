import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path("data/paper_trading.sqlite3")

def ensure_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL, ticker TEXT NOT NULL,
            side TEXT NOT NULL CHECK(side IN ('BUY','SELL')),
            quantity REAL NOT NULL CHECK(quantity > 0),
            price REAL NOT NULL CHECK(price > 0),
            notional REAL NOT NULL
        )""")
        con.commit()

class PaperBroker:
    """Local paper broker only. No exchange or brokerage API is called."""
    def submit(self, ticker: str, side: str, quantity: float, price: float):
        side = side.upper()
        if not ticker.strip() or side not in {"BUY", "SELL"}:
            raise ValueError("Ticker ou lado inválido.")
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantidade e preço devem ser positivos.")
        ensure_db()
        created = datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(DB_PATH) as con:
            cur = con.execute(
                "INSERT INTO orders(created_at,ticker,side,quantity,price,notional) VALUES(?,?,?,?,?,?)",
                (created, ticker.upper(), side, quantity, price, quantity * price)
            )
            con.commit()
            return {"id": cur.lastrowid, "created_at": created, "ticker": ticker.upper(),
                    "side": side, "quantity": quantity, "price": price, "notional": quantity * price}

    def recent_orders(self, limit: int = 25):
        ensure_db()
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = sqlite3.Row
            rows = con.execute("SELECT * FROM orders ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]

Vhalinor Finance AI

MVP de painel web para análise de ativos brasileiros, ações/ETFs dos EUA e criptoativos, simulação de juros compostos, métricas de risco e paper trading local.


Executar localmente

Python 3.11+:


python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
streamlit run app.py

Windows: .venv\Scripts\activate.


Tickers exemplo

Brasil: PETR4.SA, VALE3.SA, BOVA11.SA, ^BVSP.
Exterior: AAPL, MSFT, NVDA, SPY, QQQ.
Cripto: BTC-USD, ETH-USD, SOL-USD.


Incluído


Painel Streamlit e gráfico candlestick.

Médias móveis de 20/50 períodos, RSI(14).

Backtest didático de cruzamento de médias versus buy-and-hold.

Simulador de juros compostos com aportes mensais.

Métricas históricas de retorno e drawdown.

Livro de ordens simulado local SQLite (não conecta a corretoras).

Testes unitários.


Limitações e segurança


Este MVP não possui LSTM/Transformer treinado, aprendizado contínuo, feed profissional em tempo real, ranking global de produtos financeiros ou execução real.

Dados Yahoo Finance são para prototipagem; disponibilidade e atraso variam por ativo.

Backtest não incorpora custos, slippage, impostos nem todas as restrições de execução.

Paper trading é local e não replica perfeitamente mercado real.

Nunca armazene segredos de API no Git. Nenhuma rentabilidade é garantida.

Antes de produção: validação walk-forward, testes fora da amostra, custos realistas, logs auditáveis, limites de risco, monitoramento e revisão humana.


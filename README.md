# monopoly-bench
A simple benchmark for LLMs on Monopoly

Monopoly LLMs Benchmark
Valeriy, Sanzhar

Desc - a lightweight test suite to evaluate LLMs on monopoly by competing with each other. 

We will need:
- A fully featured monopoly simulation library (board state, auctions, trades, bankruptcy, etc.)
- An agentic harness for the models (current board representation, oponent actions, tool calls for actions on their turn)
- A benchmark runner script (runs multiple games in parallel, computes each model's elo using FFA elo algorithm.)
- DB storing all model context and game state, for each game, for further analysis later.


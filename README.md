# monopoly-bench
A simple benchmark for LLMs on Monopoly

Monopoly LLMs Benchmark  
Valeriy, Sanzhar

Desc – a lightweight test suite to evaluate LLMs on Monopoly by competing with each other.

We will need:
- A fully featured Monopoly simulation library (board state, auctions, trades, bankruptcy, etc.)
- An agentic harness for the models (current board representation, opponent actions, tool calls for actions on their turn)
- A benchmark runner script (runs multiple games in parallel, computes each model's Elo using FFA Elo algorithm)
- DB storing all model context and game state, for each game, for further analysis later

---

## The structure

### monopoly-core

Contains all files related to the Monopoly simulation. It is a pure game engine and **does not** talk to LLMs directly.

High-level API (subject to change):

- `new_game(config)` – create an initial `game_state` dict
- `step_until_decision(game_state)` – advance the game automatically until a player must choose something, returns `(state, decision)`
- `apply_decision(game_state, action)` – apply a player/agent action in response to a decision, returns updated `state`
- `legal_decision_actions(game_state, decision)` – enumerate valid actions for a given decision
- `is_terminal(game_state)` – check if the game is over
- `get_scores(game_state)` – final standings / net worth for Elo
- `get_observation(game_state, player_id)` – player-centric view of the state for the harness

Internally, mutation of `game_state` is done via a small set of helpers (e.g. move player, transfer money, change ownership). Higher-level modules like “actions” (player actions) and “cards” (Chance / Community Chest effects) call those helpers instead of poking the raw dict directly.

---

### Features we need to support (official rules)

- [ ] Rolling dice (two 6-sided), with doubles and third double in a row
- [ ] Landing on properties and paying rent
- [ ] Landing on properties and purchasing
- [ ] Auctioning
- [ ] Landing on Chance / Community Chest cards and performing that action
- [ ] Passing GO
- [ ] Landing on tax squares
- [ ] Mortgaging
- [ ] Buying houses and hotels (if available)
- [ ] Trading between players
- [ ] Bankruptcy (paying 10% tax, asset transfer)
- [ ] Jail (3 rolls / fines / “Get Out of Jail Free”)


### Data structures

We’ll implement the core without classes; game state is stored as a single `game_state` dictionary. The architecture is as stateless as possible: public functions take a `game_state`, apply rules, and return an updated `game_state`.

game_state contains:

- `config` (number of players, starting params, RNG seed, house/hotel limits)
- `players` (data for each player: piece, money, properties owned, mortgaged properties, jail status, etc.)
- `board` (defines properties, prices, rents, locations, special squares, etc.)
- `bank` (houses and hotels left in the bank; bank money counted as infinite)
- `turn` (current player, consecutive doubles, jail rolls, phase of the turn, pending decision)
- `cards` (chance and community chest decks)

All state changes go through a small set of mutation helpers inside `monopoly-core` (e.g. move player, pay rent, send to jail). This keeps the rules consistent between normal actions and card effects.


### Interaction

In Monopoly, players only take actions on their turn (or when required by another player's actions).

The core loop for the benchmark harness looks like:

1. Call `step_until_decision(game_state)`  
   - Engine runs automatic steps (dice, movement, forced payments, card draws, etc.)
   - Returns `decision` describing what the current player must choose (or `None` if the game is over)

2. The harness / LLM chooses an action based on:
   - The `decision`
   - The player’s `get_observation(game_state, player_id)`
   - The `legal_decision_actions(...)` list

3. Call `apply_decision(game_state, action)`  
   - Engine updates the state according to Monopoly rules

4. Repeat until `is_terminal(game_state)` is `True`, then call `get_scores(game_state)` to feed the Elo computation.

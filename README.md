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


## The structure:
### monopoly-core

    - Contains all files related to the monopoly simulation 
    
#### Features we need to support, in accordance with the official rules:

    -[ ] Rolling dice (two 6 sided), with doubles and third double in a row
    -[ ] Landing on properties and paying rent
    -[ ] Landing on properties and purchasing
    -[ ] Auctioning 
    -[ ] Landing on chance / community chest cards and performing that action
    -[ ] Passing go 
    -[ ] Landing on tax squares
    -[ ] Mortgaging
    -[ ] Buying houses and hotels (if available)
    -[ ] Trading between players
    -[ ] Bankruptcy (paying 10% tax)
    -[ ] Jail (3 rolls)

#### Data structures:

Will try to implement without classes, so game state will be stored as a single game state dictionary. The architecture will be as stateless as possible. Each function takes the old state, changes it, and returns the new state.

The dictionary will contain:
- config (number of players, starting params, RNG seed)
- players (data for each player. Piece, money, properties,etc)
- board (defines properties, prices, rents, locations, etc)
- bank (houses and hotels left)
- turn (current turn, consecutive doubles, jail, phase)
- cards (chance and community chest cards)


#### Interaction:
This is not a game, it's a library. In monopoly players only take actions on their turn, unless invoked by another player's actions. 

Therefore, we need to expose functions for each action a player can take on their turn. Each of those will call other  internal functions to properly update the game state / get input from other players. 
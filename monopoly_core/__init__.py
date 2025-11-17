def new_game():
    '''
    Initializes a new game of monopoly. Returns the game state.
    '''
    # return game_state
    pass


def step_until_decision(game_state):
    '''
    Steps the game until player decision is needed. (at the moment we don't store the in-between steps. Need to implement logging or something.)
    '''
    # return decision, game_state
    pass


def apply_decision(game_state, decision):
    '''
    Applies a decision to the game state.
    '''
    # return game_state
    pass


def get_observation(game_state):
    '''
    Returns a dictionary representing the current game state from a player's perspective.
    '''
    # return observation
    pass


def get_legal_actions(game_state, decision):
    '''
    Returns a list of legal actions for the decision.
    '''
    # return legal_actions
    pass


def is_game_over(game_state):
    '''
    Returns True if the game is over.
    '''
    # return is_terminal
    pass


def get_scores(game_state):
    '''
    Returns peak money for each player, properties owned and moves survived for each player (dictionary)
    '''
    # return scores
    pass

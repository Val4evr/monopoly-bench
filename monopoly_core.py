BOARD_TEMPLATE = [
    {"name": "GO", "type": "go", "price": 0, "rent": 0},
    {"name": "Mediterranean Avenue", "type": "property", "price": 60, "rent": 2},
    {"name": "Baltic Avenue", "type": "property", "price": 60, "rent": 4},
    {"name": "Income Tax", "type": "tax", "price": 0, "rent": 200},
    {"name": "Reading Railroad", "type": "property", "price": 200, "rent": 25},
]

COMMANDS = ("roll", "buy_property", "pay_rent", "end_turn")


def create_initial_state(num_players = 2):
    """Create initial players and board"""
    pass


def get_current_player(state):
    #Return the dict of the current player
    pass


def list_legal_commands(state):
    #Return all legal actions the current player may take
    pass


def apply_command(state, command, payload=None):
    #Apply a Monopoly command and modify state
    pass


def is_game_over(state):
    #Determine if the game has ended
    pass


def serialize_state(state):
    #Return a JSON-safe dict representing the entire game state
    pass

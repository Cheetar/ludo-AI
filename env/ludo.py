import random

NO_PLAYERS = 4
HOME_SIZE_PER_PLAYER = 4
NORMAL_SQUARES_SIZE_PER_PLAYER = 10
NORMAL_SQUARES_SIZE = 40
HOMES_SIZE = 16
NO_SQUARES = 56
GAME_STATE_SIZE = NO_SQUARES + 1  # 1 for dice roll result

FIRST_PLAYER = 1
SECOND_PLAYER = 2
THIRD_PLAYER = 3
FOURTH_PLAYER = 4

NULL_MOVE = 0
NO_PAWNS = 4

REROLL = 6


def roll_a_dice():
    return random.randint(1, 6)


def rotate_array(arr, size, left=1):
    if left:
        return arr[size:] + arr[:size]
    return arr[-size:] + arr[:-size]


def rotate_game_state(game_state, player_perspective, left=1):
    normal_squares = game_state[:NORMAL_SQUARES_SIZE]
    homes = game_state[NORMAL_SQUARES_SIZE:NORMAL_SQUARES_SIZE + HOMES_SIZE]
    dice_roll_result = [game_state[-1]]

    normal_squares = rotate_array(normal_squares, (player_perspective - 1) * NORMAL_SQUARES_SIZE_PER_PLAYER, left)
    homes = rotate_array(homes, (player_perspective - 1) * HOME_SIZE_PER_PLAYER, left)

    game_state = normal_squares + homes + dice_roll_result
    return game_state


def is_action_valid(game_state, action, player_to_move):
    dice_roll = game_state[-1]
    game_state = rotate_game_state(game_state, player_to_move)
    board = game_state[:NORMAL_SQUARES_SIZE + HOME_SIZE_PER_PLAYER]
    exists_valid_move = False
    pawn = 0
    for square_num in reversed(range(len(board))):
        # Is it the player's pawn
        if board[square_num] == player_to_move:
            pawn += 1
            # Not exceed the board
            if square_num + dice_roll < NORMAL_SQUARES_SIZE + HOME_SIZE_PER_PLAYER:
                # Not jumping over other pawns at home
                if player_to_move not in board[max(square_num + 1, NORMAL_SQUARES_SIZE):square_num + dice_roll + 1]:
                    exists_valid_move = True
                    # If player wanted to move this pawn
                    if action == pawn:
                        return True

    # If player wanted to move a pawn that he can't move
    if action != NULL_MOVE and action <= pawn:
        return False
    # Putting a pawn out of jain is a valid move
    elif dice_roll == REROLL and pawn != NO_PAWNS:
        exists_valid_move = True
        if action != NULL_MOVE:
            return True
    elif action == NULL_MOVE:
        return not exists_valid_move


def get_random_action(game_state, player_to_move):
    for action in range(5):
        if is_action_valid(game_state, action, player_to_move):
            return action


class Ludo:

    def __init__(self):
        """ Game state is an array of size equal to number of squares in the
            game (including home squares) + 1 (for dice roll result).
            0 symbolises that no pawn is at the location wheras number [1, 4]
            says that the pawn of a given player is at the location.

            The first 40 numbers represents the normal squares (counting from
            the starting point of the first player). The next 16 represents
            homes of first, second, third and fourth player respectively.

            _no_pawns is the number of pawns that left the jail for each player
        """
        self._game_state = [0] * GAME_STATE_SIZE
        self._no_pawns = [0] * NO_PLAYERS
        self._turn = 0
        self._player_to_move = FIRST_PLAYER

    def get_state(self, player_perspective=FIRST_PLAYER):
        """ Returns the game state. The array is transformed in such a way that
            every player can see the board as if they are the first player.
        """
        return (self._player_to_move, rotate_game_state(self._game_state, player_perspective))

    def initialize(self):
        self._game_state[-1] = roll_a_dice()
        return self.get_state(FIRST_PLAYER)

    def execute_action(self, action):
        if action != NULL_MOVE:
            dice_roll = self._game_state[-1]
            game_state = rotate_game_state(self._game_state, self._player_to_move)
            board = game_state[:NORMAL_SQUARES_SIZE + HOME_SIZE_PER_PLAYER]
            pawn = 0
            for square_num in reversed(range(len(board))):
                if board[square_num] == self._player_to_move:
                    pawn += 1
                    if action == pawn:
                        board[square_num] = 0
                        board[square_num + dice_roll] = self._player_to_move

            if action > pawn and dice_roll == REROLL:
                board[0] = self._player_to_move

            game_state = board + game_state[len(board):]
            self._game_state = rotate_game_state(game_state, self._player_to_move, 0)

    def update_game_state(self):
        dice_roll = self._game_state[-1]
        if dice_roll != REROLL:
            self._turn += 1
            self._player_to_move = (self._player_to_move % NO_PLAYERS) + 1

        self._game_state[-1] = roll_a_dice()

    def has_game_ended(self):
        return 0 not in self._game_state[NORMAL_SQUARES_SIZE:NORMAL_SQUARES_SIZE + HOMES_SIZE]

    def step(self, action):
        if self.has_game_ended():
            return None

        if not is_action_valid(self._game_state, action, self._player_to_move):
            action = get_random_action(self._game_state, self._player_to_move)

        self.execute_action(action)
        self.update_game_state()
        if self.has_game_ended():
            return None

        return self.get_state(self._player_to_move)

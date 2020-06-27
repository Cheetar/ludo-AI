import unittest

from ludo import is_action_valid


class TestIsActionValid(unittest.TestCase):

    def test_pawn_at_third_square_at_home_dice_roll_1(self):
        game_state = [0] * 57
        game_state[-1] = 1
        game_state[40 + 2] = 1
        self.assertTrue(is_action_valid(game_state, 1, 1))

    def test_moving_not_valid_last_square_at_home(self):
        game_state = [0] * 57
        game_state[-1] = 1
        game_state[40 + 3] = 1
        self.assertFalse(is_action_valid(game_state, 1, 1))

    def test_leave_jail_pawn_at_home(self):
        game_state = [0] * 57
        game_state[-1] = 6
        game_state[40 + 3] = 1
        self.assertFalse(is_action_valid(game_state, 0, 1))
        self.assertFalse(is_action_valid(game_state, 1, 1))
        self.assertTrue(is_action_valid(game_state, 2, 1))
        self.assertTrue(is_action_valid(game_state, 3, 1))
        self.assertTrue(is_action_valid(game_state, 4, 1))

    def test_leaving_jail(self):
        game_state = [0] * 57
        game_state[-1] = 6
        self.assertFalse(is_action_valid(game_state, 0, 1))
        self.assertTrue(is_action_valid(game_state, 1, 1))
        self.assertTrue(is_action_valid(game_state, 2, 1))
        self.assertTrue(is_action_valid(game_state, 3, 1))
        self.assertTrue(is_action_valid(game_state, 4, 1))

    def test_not_jumping_over_at_home(self):
        game_state = [0] * 57
        game_state[-1] = 2
        game_state[40 + 1]
        game_state[40 + 2]
        self.assertTrue(is_action_valid(game_state, 0, 1))
        self.assertFalse(is_action_valid(game_state, 1, 1))
        self.assertFalse(is_action_valid(game_state, 2, 1))
        self.assertFalse(is_action_valid(game_state, 3, 1))
        self.assertFalse(is_action_valid(game_state, 4, 1))


if __name__ == '__main__':
    unittest.main()

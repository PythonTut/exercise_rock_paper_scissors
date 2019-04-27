from unittest import TestCase
from up_and_down import landing_spot, best_dice_roll, best_strategy, probability_landing_spot


class LadderGameTest(TestCase):

    def test_landing_spot(self):
        # Without any ladders in between
        self.assertEqual(5, landing_spot(1, 4))
        self.assertEqual(12, landing_spot(7, 5))

        # Over 100
        self.assertEqual(97, landing_spot(97, 6))
        self.assertEqual(99, landing_spot(95, 6))

        # Ladders in between but not taken
        self.assertEqual(8, landing_spot(4, 4))
        self.assertEqual(52, landing_spot(49, 3))

        # Multiple ladders in between not taken
        self.assertEqual(22, landing_spot(17, 5))
        self.assertEqual(43, landing_spot(37, 6))

        # Ladder up
        self.assertEqual(98, landing_spot(91, 1))
        self.assertEqual(85, landing_spot(60, 5))

        # Ladder down
        self.assertEqual(92, landing_spot(95, 3))
        self.assertEqual(31, landing_spot(36, 6))
        self.assertEqual(21, landing_spot(51, 2))

        # Over 100, ladder 98 down
        self.assertEqual(92, landing_spot(96, 6))
        self.assertEqual(92, landing_spot(99, 3))

    def test_best_dice_roll(self):
        # No ladder in between
        self.assertEqual((6, 13), best_dice_roll(7))
        self.assertEqual((6, 91), best_dice_roll(85))

        # Only ladder downwards in between
        self.assertEqual((6, 29), best_dice_roll(23))
        self.assertEqual((6, 44), best_dice_roll(38))

        # One Ladder upwards
        self.assertEqual((3, 27), best_dice_roll(3))
        self.assertEqual((5, 98), best_dice_roll(87))

        # Ladder up and down
        self.assertEqual((3, 53), best_dice_roll(18))
        self.assertEqual((4, 85), best_dice_roll(61))

        # Multiple ladders upwards
        self.assertEqual((2, 80), best_dice_roll(66))
        self.assertEqual((1, 42), best_dice_roll(30))

    def test_best_strategy(self):
        self.assertEqual([6, 4, 4, 3, 6, 1, 2], best_strategy(0))
        self.assertEqual([6, 2, 4, 3, 6, 1, 2], best_strategy(23))
        self.assertEqual([1, 4, 3, 6, 1, 2], best_strategy(30))

    def test_probability_landing_spot(self):
        self.assertEqual({1: 1 / 6, 2: 1 / 6, 3: 1 / 6, 4: 1 / 6, 5: 1 / 6, 27: 1 / 6},
                         probability_landing_spot(0, [6, 6, 6, 6, 6, 6]))

        self.assertEqual({1: 1 / 18, 2: 1 / 18, 3: 1 / 18, 4: 1 / 18, 5: 1 / 18, 27: 13 / 18},
                         probability_landing_spot(0, [2, 2, 2, 2, 2, 26]))

        self.assertEqual({42: 1 / 3, 32: 1 / 3, 38: 1 / 3, 34: 0.0, 35: 0.0, 36: 0.0},
                         probability_landing_spot(30, [12, 12, 12, 0, 0, 0]))

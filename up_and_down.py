from typing import List, Tuple, Dict

ladders: List[Tuple[int, int]] = [
    (6, 27), (14, 19), (21, 53), (31, 42), (33, 38), (46, 62),
    (51, 59), (57, 96), (65, 85), (68, 80), (70, 76), (92, 98)
]

result_not_biased_dice: List[int] = [6, 6, 6, 6, 6, 6]
result_first_biased_dice: List[int] = [2, 2, 2, 2, 2, 26]
result_second_biased_dice: List[int] = [12, 12, 12, 0, 0, 0]


def landing_spot(start: int, eyes: int) -> int:
    # TODO implement function
    pass


def best_dice_roll(start: int) -> Tuple[int, int]:
    # TODO implement function
    pass


def best_strategy(start: int) -> List[int]:
    # TODO implement function
    pass


def probability_landing_spot(start: int, dice_probabilities: List[int]) -> Dict[int, float]:
    # TODO implement function
    pass

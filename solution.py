from typing import List, Tuple, Dict

ladders: List[Tuple[int, int]] = [
    (6, 27), (14, 19), (21, 53), (31, 42), (33, 38), (46, 62),
    (51, 59), (57, 96), (65, 85), (68, 80), (70, 76), (92, 98)
]


def landing_spot(start: int, eyes: int) -> int:
    direct_spot = start + eyes

    if direct_spot > 100:
        direct_spot = 200 - direct_spot  # == 100 - (direct_spot - 100)

    for (ladder_start, ladder_target) in ladders:
        if direct_spot == ladder_start:
            return ladder_target
        elif direct_spot == ladder_target:
            return ladder_start

    return direct_spot


def best_dice_roll(start: int) -> Tuple[int, int]:
    best_eyes: int = 0
    best_landing_spot: int = 0

    for eyes in [1, 2, 3, 4, 5, 6]:
        land_spot = landing_spot(start, eyes)
        if land_spot > best_landing_spot:
            best_eyes = eyes
            best_landing_spot = land_spot

    return best_eyes, best_landing_spot


def optimal_way_eyes(start: int) -> List[int]:
    current_spot = start
    eyes: List[int] = []

    while current_spot != 100:
        rolled, current_spot = best_dice_roll(current_spot)
        eyes.append(rolled)

    return eyes


def probable_landing_spot(start: int, dice_probabilities: List[int]) -> Dict[int, float]:
    tries: int = sum(dice_probabilities)

    probable_fields: Dict[int, float] = {}
    for (eyes_minus_1, eye_tries) in enumerate(dice_probabilities):
        land_spot = landing_spot(start, eyes_minus_1 + 1)
        probable_fields[land_spot] = eye_tries / tries

    return probable_fields

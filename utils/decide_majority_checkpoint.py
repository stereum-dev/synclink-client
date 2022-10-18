import math

from utils import hex_to_dec_string

checkpoints_repeats = {}

checkpoints = []


def generate_key(checkpoint):
    key_chunk_0 = hex_to_dec_string(checkpoint["previous_justified"]["root"])
    key_chunk_1 = hex_to_dec_string(checkpoint["current_justified"]["root"])
    key_chunk_2 = hex_to_dec_string(checkpoint["finalized"]["root"])

    key = f"{key_chunk_0}-{key_chunk_1}_{key_chunk_2}"

    return key


for checkpoint in checkpoints:
    key = generate_key(checkpoint)
    if key in checkpoints_repeats:
        checkpoints_repeats[key]["count"] += 1
    else:
        checkpoints_repeats[key] = {
            "finality": checkpoint,
            "count": 1
        }

    for _, value in checkpoints_repeats.items():
        if (value['count'] > math.floor(len(checkpoints) / 2)):
            print(value['finality'])

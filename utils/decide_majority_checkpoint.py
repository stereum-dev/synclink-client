import math
from typing import List

from models.get_state_finality_checkpoints_response_data import \
    GetStateFinalityCheckpointsResponseData

from utils.eth import hex_to_dec_string


def generate_key(checkpoint: GetStateFinalityCheckpointsResponseData):
    key_chunk_0 = hex_to_dec_string(checkpoint.previous_justified.root)
    key_chunk_1 = hex_to_dec_string(checkpoint.current_justified.root)
    key_chunk_2 = hex_to_dec_string(checkpoint.finalized.root)

    key = f"{key_chunk_0}-{key_chunk_1}_{key_chunk_2}"

    return key


def decide_majority_checkpoint(checkpoints: List[GetStateFinalityCheckpointsResponseData]) -> GetStateFinalityCheckpointsResponseData:
    checkpoints_repeats = {}

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
                return (value['finality'])

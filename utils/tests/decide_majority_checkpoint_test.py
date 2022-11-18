import pytest

from models.get_state_finality_checkpoints_response_data import \
    GetStateFinalityCheckpointsResponseData as Finality
from models.get_state_finality_checkpoints_response_data_previous_justified import \
    GetStateFinalityCheckpointsResponseDataPreviousJustified as Justified
from utils.decide_majority_checkpoint import decide_majority_checkpoint


def test_one_node():
    finality = Finality(
        previous_justified=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"),
        current_justified=Justified(
            epoch="136078", root="0xb1c30a87b23abd9f58b48ba25f6ccdd05f6c74f52b64fb75b7745faef8d238d7"),
        finalized=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"))

    syncpoint = decide_majority_checkpoint(checkpoints=[finality])

    assert syncpoint == finality


def test_three_node():
    finality_0 = Finality(
        previous_justified=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"),
        current_justified=Justified(
            epoch="136078", root="0xb1c30a87b23abd9f58b48ba25f6ccdd05f6c74f52b64fb75b7745faef8d238d7"),
        finalized=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"))

    finality_1 = Finality(
        previous_justified=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"),
        current_justified=Justified(
            epoch="136078", root="0xb1c30a87b23abd9f58b48ba25f6ccdd05f6c74f52b64fb75b7745faef8d238d7"),
        finalized=Justified(
            epoch="136077", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d8e"))

    finality_2 = Finality(
        previous_justified=Justified(
            epoch="136078", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d9e"),
        current_justified=Justified(
            epoch="136079", root="0xb1c30a87b23abd9f58b48ba25f6ccdd05f6c74f52b64fb75b7745faef8d238c7"),
        finalized=Justified(
            epoch="136078", root="0x3e825e6c18d217fd27f0fbef3fa6e0b15047bb062471cbe89944772b74876d9e"))

    syncpoint = decide_majority_checkpoint(
        checkpoints=[finality_0, finality_1, finality_2])

    assert syncpoint == finality_0 == finality_1 != finality_2

# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AltairSyncCommitteeContribution(BaseModel):
    """AltairSyncCommitteeContribution - a model defined in OpenAPI

        slot: The slot of this AltairSyncCommitteeContribution [Optional].
        beacon_block_root: The beacon_block_root of this AltairSyncCommitteeContribution [Optional].
        subcommittee_index: The subcommittee_index of this AltairSyncCommitteeContribution [Optional].
        aggregation_bits: The aggregation_bits of this AltairSyncCommitteeContribution [Optional].
        signature: The signature of this AltairSyncCommitteeContribution [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    beacon_block_root: Optional[str] = Field(alias="beacon_block_root", default=None)
    subcommittee_index: Optional[str] = Field(alias="subcommittee_index", default=None)
    aggregation_bits: Optional[object] = Field(alias="aggregation_bits", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

AltairSyncCommitteeContribution.update_forward_refs()

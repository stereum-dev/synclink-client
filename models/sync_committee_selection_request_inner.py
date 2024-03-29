# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SyncCommitteeSelectionRequestInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SyncCommitteeSelectionRequestInner - a model defined in OpenAPI

        validator_index: The validator_index of this SyncCommitteeSelectionRequestInner [Optional].
        slot: The slot of this SyncCommitteeSelectionRequestInner [Optional].
        subcommittee_index: The subcommittee_index of this SyncCommitteeSelectionRequestInner [Optional].
        selection_proof: The selection_proof of this SyncCommitteeSelectionRequestInner [Optional].
    """

    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)
    subcommittee_index: Optional[str] = Field(alias="subcommittee_index", default=None)
    selection_proof: Optional[str] = Field(alias="selection_proof", default=None)

SyncCommitteeSelectionRequestInner.update_forward_refs()

# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetEpochCommitteesResponseDataInner(BaseModel):
    """GetEpochCommitteesResponseDataInner - a model defined in OpenAPI

        index: The index of this GetEpochCommitteesResponseDataInner [Optional].
        slot: The slot of this GetEpochCommitteesResponseDataInner [Optional].
        validators: The validators of this GetEpochCommitteesResponseDataInner [Optional].
    """

    index: Optional[str] = Field(alias="index", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)
    validators: Optional[List[str]] = Field(alias="validators", default=None)

GetEpochCommitteesResponseDataInner.update_forward_refs()

# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetBlockHeadersResponseDataInnerHeaderMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetBlockHeadersResponseDataInnerHeaderMessage - a model defined in OpenAPI

        slot: The slot of this GetBlockHeadersResponseDataInnerHeaderMessage [Optional].
        proposer_index: The proposer_index of this GetBlockHeadersResponseDataInnerHeaderMessage [Optional].
        parent_root: The parent_root of this GetBlockHeadersResponseDataInnerHeaderMessage [Optional].
        state_root: The state_root of this GetBlockHeadersResponseDataInnerHeaderMessage [Optional].
        body_root: The body_root of this GetBlockHeadersResponseDataInnerHeaderMessage [Optional].
    """

    slot: Optional[str] = Field(alias="slot", default=None)
    proposer_index: Optional[str] = Field(alias="proposer_index", default=None)
    parent_root: Optional[str] = Field(alias="parent_root", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    body_root: Optional[str] = Field(alias="body_root", default=None)

GetBlockHeadersResponseDataInnerHeaderMessage.update_forward_refs()

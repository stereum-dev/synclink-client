# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class BeaconBlockAllOfBodyEth1Data(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    BeaconBlockAllOfBodyEth1Data - a model defined in OpenAPI

        deposit_root: The deposit_root of this BeaconBlockAllOfBodyEth1Data [Optional].
        deposit_count: The deposit_count of this BeaconBlockAllOfBodyEth1Data [Optional].
        block_hash: The block_hash of this BeaconBlockAllOfBodyEth1Data [Optional].
    """

    deposit_root: Optional[str] = Field(alias="deposit_root", default=None)
    deposit_count: Optional[str] = Field(alias="deposit_count", default=None)
    block_hash: Optional[str] = Field(alias="block_hash", default=None)

BeaconBlockAllOfBodyEth1Data.update_forward_refs()
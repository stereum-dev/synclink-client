# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SubscribeToBeaconCommitteeSubnetRequestBodyInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubscribeToBeaconCommitteeSubnetRequestBodyInner - a model defined in OpenAPI

        validator_index: The validator_index of this SubscribeToBeaconCommitteeSubnetRequestBodyInner [Optional].
        committee_index: The committee_index of this SubscribeToBeaconCommitteeSubnetRequestBodyInner [Optional].
        committees_at_slot: The committees_at_slot of this SubscribeToBeaconCommitteeSubnetRequestBodyInner [Optional].
        slot: The slot of this SubscribeToBeaconCommitteeSubnetRequestBodyInner [Optional].
        is_aggregator: The is_aggregator of this SubscribeToBeaconCommitteeSubnetRequestBodyInner [Optional].
    """

    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    committee_index: Optional[str] = Field(alias="committee_index", default=None)
    committees_at_slot: Optional[str] = Field(alias="committees_at_slot", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)
    is_aggregator: Optional[bool] = Field(alias="is_aggregator", default=None)

SubscribeToBeaconCommitteeSubnetRequestBodyInner.update_forward_refs()

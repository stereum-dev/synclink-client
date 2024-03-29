# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_attestations_rewards_response_data import GetAttestationsRewardsResponseData


class GetAttestationsRewardsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetAttestationsRewardsResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetAttestationsRewardsResponse [Optional].
        finalized: The finalized of this GetAttestationsRewardsResponse [Optional].
        data: The data of this GetAttestationsRewardsResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    finalized: Optional[bool] = Field(alias="finalized", default=None)
    data: Optional[GetAttestationsRewardsResponseData] = Field(alias="data", default=None)

GetAttestationsRewardsResponse.update_forward_refs()

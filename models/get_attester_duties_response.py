# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_attester_duties_response_data_inner import GetAttesterDutiesResponseDataInner


class GetAttesterDutiesResponse(BaseModel):
    """GetAttesterDutiesResponse - a model defined in OpenAPI

        dependent_root: The dependent_root of this GetAttesterDutiesResponse [Optional].
        execution_optimistic: The execution_optimistic of this GetAttesterDutiesResponse [Optional].
        data: The data of this GetAttesterDutiesResponse [Optional].
    """

    dependent_root: Optional[str] = Field(alias="dependent_root", default=None)
    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[List[GetAttesterDutiesResponseDataInner]] = Field(alias="data", default=None)

GetAttesterDutiesResponse.update_forward_refs()

# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_fork_response_data import GetStateForkResponseData


class GetForkScheduleResponse(BaseModel):
    """GetForkScheduleResponse - a model defined in OpenAPI

        data: The data of this GetForkScheduleResponse [Optional].
    """

    data: Optional[List[GetStateForkResponseData]] = Field(alias="data", default=None)

GetForkScheduleResponse.update_forward_refs()

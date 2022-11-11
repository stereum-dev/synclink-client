# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ValidatorBalanceResponse(BaseModel):
    """ValidatorBalanceResponse - a model defined in OpenAPI

        index: The index of this ValidatorBalanceResponse [Optional].
        balance: The balance of this ValidatorBalanceResponse [Optional].
    """

    index: Optional[str] = Field(alias="index", default=None)
    balance: Optional[str] = Field(alias="balance", default=None)

ValidatorBalanceResponse.update_forward_refs()

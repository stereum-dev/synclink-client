# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SubmitPoolAttestations400ResponseFailuresInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubmitPoolAttestations400ResponseFailuresInner - a model defined in OpenAPI

        index: The index of this SubmitPoolAttestations400ResponseFailuresInner [Optional].
        message: The message of this SubmitPoolAttestations400ResponseFailuresInner [Optional].
    """

    index: Optional[float] = Field(alias="index", default=None)
    message: Optional[str] = Field(alias="message", default=None)

SubmitPoolAttestations400ResponseFailuresInner.update_forward_refs()

# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.beacon_committee_selection_request_inner import BeaconCommitteeSelectionRequestInner


class BeaconCommitteeSelectionResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    BeaconCommitteeSelectionResponse - a model defined in OpenAPI

        data: The data of this BeaconCommitteeSelectionResponse [Optional].
    """

    data: Optional[List[BeaconCommitteeSelectionRequestInner]] = Field(alias="data", default=None)

BeaconCommitteeSelectionResponse.update_forward_refs()
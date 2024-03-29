# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner_header import GetBlockHeadersResponseDataInnerHeader


class PublishBlindedBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishBlindedBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner - a model defined in OpenAPI

        signed_header_1: The signed_header_1 of this PublishBlindedBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner [Optional].
        signed_header_2: The signed_header_2 of this PublishBlindedBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner [Optional].
    """

    signed_header_1: Optional[GetBlockHeadersResponseDataInnerHeader] = Field(alias="signed_header_1", default=None)
    signed_header_2: Optional[GetBlockHeadersResponseDataInnerHeader] = Field(alias="signed_header_2", default=None)

PublishBlindedBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner.update_forward_refs()

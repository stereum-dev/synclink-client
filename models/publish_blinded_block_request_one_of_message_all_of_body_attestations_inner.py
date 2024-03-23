# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of_message_all_of_body_attester_slashings_inner_attestation1_data import PublishBlindedBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data


class PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner - a model defined in OpenAPI

        aggregation_bits: The aggregation_bits of this PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner [Optional].
        signature: The signature of this PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner [Optional].
        data: The data of this PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner [Optional].
    """

    aggregation_bits: Optional[str] = Field(alias="aggregation_bits", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)
    data: Optional[PublishBlindedBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInnerAttestation1Data] = Field(alias="data", default=None)

    @validator("aggregation_bits")
    def aggregation_bits_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]+$", value)
        return value

PublishBlindedBlockRequestOneOfMessageAllOfBodyAttestationsInner.update_forward_refs()
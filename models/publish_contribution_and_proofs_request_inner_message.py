# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.produce_sync_committee_contribution_response_data import ProduceSyncCommitteeContributionResponseData


class PublishContributionAndProofsRequestInnerMessage(BaseModel):
    """PublishContributionAndProofsRequestInnerMessage - a model defined in OpenAPI

        aggregator_index: The aggregator_index of this PublishContributionAndProofsRequestInnerMessage [Optional].
        selection_proof: The selection_proof of this PublishContributionAndProofsRequestInnerMessage [Optional].
        contribution: The contribution of this PublishContributionAndProofsRequestInnerMessage [Optional].
    """

    aggregator_index: Optional[str] = Field(alias="aggregator_index", default=None)
    selection_proof: Optional[str] = Field(alias="selection_proof", default=None)
    contribution: Optional[ProduceSyncCommitteeContributionResponseData] = Field(alias="contribution", default=None)

    @validator("selection_proof")
    def selection_proof_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishContributionAndProofsRequestInnerMessage.update_forward_refs()

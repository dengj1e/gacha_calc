"""
defines and validates the structure of our data type
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class GameId(str, Enum):
    genshin = "genshin"
    hsr     = "hsr"
    zzz     = "zzz"


class CalculateRequest(BaseModel):
    game:      GameId
    pity:      int = Field(ge=0, le=89)
    pulls:     int = Field(ge=1, le=2000)
    guaranteed: bool = False
    copies:    int = Field(ge=1, le=7)


class CalculationResponse(BaseModel):
    id:                int
    game:              str
    pity:              int
    pulls:             int
    guaranteed:        bool
    copies:            int
    probability:       float
    expected_pulls:    int
    currency_cost:     int
    pulls_to_hard_pity: int
    created_at:        datetime

    class Config:
        from_attributes = True  # lets Pydantic read SQLAlchemy objects

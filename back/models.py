"""
defines our database
"""

from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, func
from database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id             = Column(Integer, primary_key=True, index=True)
    game           = Column(String)
    pity           = Column(Integer)
    pulls          = Column(Integer)
    guaranteed     = Column(Boolean)
    copies         = Column(Integer)
    probability    = Column(Float)
    expected_pulls = Column(Integer)
    currency_cost  = Column(Integer)
    pulls_to_hard_pity = Column(Integer)
    created_at     = Column(DateTime, server_default=func.now())
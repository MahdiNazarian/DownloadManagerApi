from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER


class DbBaseModel:
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False)
    Deleted = Column(Boolean, default=False, nullable=False)

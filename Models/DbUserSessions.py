import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbUserSessions(Base):
    __tablename__ = "DbUserSessions"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    Token = Column(NVARCHAR, default="", nullable=False)
    CreatedOnUtc = Column(DATETIME2, default=datetime.datetime.now(), nullable=False)
    ExpireDate = Column(DATETIME2, default=datetime.datetime.now(), nullable=False)
    User = relationship("DbUser")

    @staticmethod
    def from_json_update(json_dct):
        return DbUserSessions(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            Token=json_dct["Token"],
            CreatedOnUtc=json_dct["CreatedOnUtc"],
            ExpireDate=json_dct["ExpireDate"]
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbUserSessions(
            UserId=json_dct["UserId"],
            Token=json_dct["Token"],
            CreatedOnUtc=json_dct["CreatedOnUtc"],
            ExpireDate=json_dct["ExpireDate"]
        )

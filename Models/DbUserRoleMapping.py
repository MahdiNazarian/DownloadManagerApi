import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbUserRoleMapping(Base):
    __tablename__ = "DbUserRoleMapping"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    RoleId = Column(BigInteger, ForeignKey("DbRole.Id"), nullable=False)
    User = relationship("DbUser")
    Role = relationship("DbRole")

    @staticmethod
    def from_json_update(json_dct):
        return DbUserRoleMapping(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            RoleId=json_dct["RoleId"]
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbUserRoleMapping(
            UserId=json_dct["UserId"],
            RoleId=json_dct["RoleId"]
        )

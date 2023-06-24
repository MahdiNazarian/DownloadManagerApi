import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base
from Models import DbBaseModel
import hashlib


class DbUser(Base):
    __tablename__ = "DbUsers"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    Email = Column(NVARCHAR, nullable=False)
    FirstName = Column(NVARCHAR, nullable=False, default="")
    LastName = Column(NVARCHAR, nullable=False, default="")
    IsEmailConfirmed = Column(Boolean, nullable=False, default=False)
    PhoneNumber = Column(NVARCHAR, nullable=False)
    IsPhoneNumberConfirmed = Column(Boolean, nullable=False, default=False)
    Password = Column(NVARCHAR, nullable=False, default="")
    LastLogin = Column(DATETIME2, nullable=False, default=datetime.datetime.now())

    @staticmethod
    def from_json_update(json_dct):
        return DbUser(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            Email=json_dct["Email"],
            FirstName=json_dct["FirstName"],
            LastName=json_dct["LastName"],
            IsEmailConfirmed=json_dct["IsEmailConfirmed"],
            PhoneNumber=json_dct["PhoneNumber"],
            IsPhoneNumberConfirmed=json_dct["IsPhoneNumberConfirmed"],
            Password=hashlib.md5(json_dct["Password"].encode('utf-8')).hexdigest(),
            LastLogin=json_dct["LastLogin"]
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbUser(
            Email=json_dct["Email"],
            FirstName=json_dct["FirstName"],
            LastName=json_dct["LastName"],
            IsEmailConfirmed=json_dct["IsEmailConfirmed"],
            PhoneNumber=json_dct["PhoneNumber"],
            IsPhoneNumberConfirmed=json_dct["IsPhoneNumberConfirmed"],
            Password=hashlib.md5(json_dct["Password"].encode('utf-8')).hexdigest()
        )

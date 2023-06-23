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
    def custom_from_json(json_dct):
        return DbUser(
            Id=json_dct["Id"],
            GuId=uuid.UUID(json_dct["GuId"]),
            Deleted=json_dct["Deleted"],
            Email=json_dct["Email"],
            FirstName=json_dct["FirstName"],
            LastName=json_dct["LastName"],
            IsEmailConfirmed=json_dct["IsEmailConfirmed"],
            PhoneNumber=json_dct["PhoneNumber"],
            IsPhoneNumberConfirmed=json_dct["IsPhoneNumberConfirmed"],
            Password=hashlib.md5(json_dct["Password"]).hexdigest(),
            LastLogin=json_dct["LastLogin"]
        )

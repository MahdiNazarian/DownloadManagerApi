from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mssql import DATETIME2
import datetime
from DbContext.DbContext import Base
from Models import DbBaseModel


class DbUser(DbBaseModel, Base):
    __tablename__ = "DbUsers"

    Email = Column(String, index=True, nullable=False)
    FirstName = Column(String, nullable=False, default="")
    LastName = Column(String, nullable=False, default="")
    IsEmailConfirmed = Column(Boolean, nullable=False, default=False)
    PhoneNumber = Column(String, nullable=False, index=True)
    IsPhoneNumberConfirmed = Column(Boolean, nullable=False, default=False)
    Password = Column(String, nullable=False, default="")
    LasLogin = Column(DATETIME2, nullable=False, default=datetime.datetime.now())

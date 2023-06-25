import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbUserSubscriptions(Base):
    __tablename__ = "DbUserSubscriptions"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    SubscriptionTypeId = Column(BigInteger, ForeignKey("DbSubscriptionTypes.Id"), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    SubscriptionBuyDate = Column(DATETIME2, nullable=False, default=datetime.datetime.now())
    SubscriptionEndDate = Column(DATETIME2, nullable=False, default=datetime.datetime.now())
    SubscriptionType = relationship("DbSubscriptionTypes")
    User = relationship("DbUser")

    @staticmethod
    def from_json_update(json_dct):
        return DbUserSubscriptions(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            SubscriptionTypeId=json_dct["SubscriptionTypeId"],
            active=json_dct["active"],
            SubscriptionBuyDate=json_dct["SubscriptionBuyDate"],
            SubscriptionEndDate=json_dct["SubscriptionEndDate"],
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbUserSubscriptions(
            UserId=json_dct["UserId"],
            SubscriptionTypeId=json_dct["SubscriptionTypeId"],
            active=json_dct["active"],
            SubscriptionBuyDate=json_dct["SubscriptionBuyDate"],
            SubscriptionEndDate=json_dct["SubscriptionEndDate"],
        )

import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbUserSettings(Base):
    __tablename__ = "DbUserSettings"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    UserSettingSubjectId = Column(BigInteger, ForeignKey("DbUserSettingSubjects.Id"), nullable=False)
    SettingName = Column(NVARCHAR, default="", nullable=False)
    SettingValue = Column(NVARCHAR, default="", nullable=False)
    SettingDesc = Column(NVARCHAR, default="", nullable=False)
    User = relationship("DbUser")
    UserSettingSubject = relationship("DbUserSettingSubjects")

    @staticmethod
    def from_json_update(json_dct):
        return DbUserSettings(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            UserSettingSubjectId=json_dct["UserSettingSubjectId"],
            SettingName=json_dct["SettingName"],
            SettingValue=json_dct["SettingValue"],
            SettingDesc=json_dct["SettingDesc"],
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbUserSettings(
            UserId=json_dct["UserId"],
            UserSettingSubjectId=json_dct["UserSettingSubjectId"],
            SettingName=json_dct["SettingName"],
            SettingValue=json_dct["SettingValue"],
            SettingDesc=json_dct["SettingDesc"],
        )

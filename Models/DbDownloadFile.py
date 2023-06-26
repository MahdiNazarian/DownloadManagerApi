import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbDownloadFile(Base):
    __tablename__ = "DbDownloadFile"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    DownloadLineId = Column(BigInteger, ForeignKey("DbDownloadLine.Id"), nullable=False)
    FileName = Column(NVARCHAR, default="", nullable=False)
    FileSize = Column(BigInteger, default=0, nullable=False)
    DownloadPath = Column(NVARCHAR, default="", nullable=False)
    DownloadStatus = Column(NVARCHAR, default="", nullable=False)
    RemainingTime = Column(BigInteger, default=0, nullable=False)
    DownloadedSize = Column(BigInteger, default=0, nullable=False)
    HasSpeedLimit = Column(Boolean, default=False, nullable=False)
    DownloadSpeed = Column(BigInteger, default=0, nullable=False)
    Description = Column(NVARCHAR, default="", nullable=False)
    DownloadLine = relationship("DbDownloadLine")

    @staticmethod
    def from_json_update(json_dct):
        return DbDownloadFile(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            DownloadLineId=json_dct["DownloadLineId"],
            FileName=json_dct["FileName"],
            FileSize=json_dct["FileSize"],
            DownloadPath=json_dct["DownloadPath"],
            DownloadStatus=json_dct["DownloadStatus"],
            RemainingTime=json_dct["RemainingTime"],
            DownloadedSize=json_dct["DownloadedSize"],
            HasSpeedLimit=json_dct["HasSpeedLimit"],
            DownloadSpeed=json_dct["DownloadSpeed"],
            Description=json_dct["Description"],
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbDownloadFile(
            DownloadLineId=json_dct["DownloadLineId"],
            FileName=json_dct["FileName"],
            FileSize=json_dct["FileSize"],
            DownloadPath=json_dct["DownloadPath"],
            DownloadStatus=json_dct["DownloadStatus"],
            RemainingTime=json_dct["RemainingTime"],
            DownloadedSize=json_dct["DownloadedSize"],
            HasSpeedLimit=json_dct["HasSpeedLimit"],
            DownloadSpeed=json_dct["DownloadSpeed"],
            Description=json_dct["Description"],
        )

import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbTiming(Base):
    __tablename__ = "DbTiming"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    SpeedLimited = Column(Boolean, default=False, nullable=False)
    DisconnectAfterCompletion = Column(Boolean, default=False, nullable=False)
    RetryCount = Column(Integer, default=0, nullable=False)
    DownloadDate = Column(DATETIME2, default=datetime.datetime.now(), nullable=False)
    DailyDownload = Column(Boolean, default=False, nullable=False)
    StartHour = Column(NVARCHAR, default="00:00", nullable=False)
    EndHour = Column(NVARCHAR, default="00:00", nullable=False)
    StartDownloadOnProgramStartup = Column(Boolean, default=False, nullable=False)
    DownloadSpeed = Column(BigInteger, default=0, nullable=False)
    CloseProgramAfterDownload = Column(Boolean, default=False, nullable=False)
    ShutDownSystemAfterDownloads = Column(Boolean, default=False, nullable=False)
    CreatedOnUtc = Column(DATETIME2, default=datetime.datetime.now(), nullable=False)
    User = relationship("DbUser")

    @staticmethod
    def from_json_update(json_dct):
        return DbTiming(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            SpeedLimited=json_dct["SpeedLimited"],
            DisconnectAfterCompletion=json_dct["DisconnectAfterCompletion"],
            RetryCount=json_dct["RetryCount"],
            DownloadDate=json_dct["DownloadDate"],
            DailyDownload=json_dct["DailyDownload"],
            StartHour=json_dct["StartHour"],
            EndHour=json_dct["EndHour"],
            StartDownloadOnProgramStartup=json_dct["StartDownloadOnProgramStartup"],
            DownloadSpeed=json_dct["DownloadSpeed"],
            CloseProgramAfterDownload=json_dct["CloseProgramAfterDownload"],
            ShutDownSystemAfterDownloads=json_dct["ShutDownSystemAfterDownloads"],
            CreatedOnUtc=json_dct["CreatedOnUtc"]
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbTiming(
            UserId=json_dct["UserId"],
            SpeedLimited=json_dct["SpeedLimited"],
            DisconnectAfterCompletion=json_dct["DisconnectAfterCompletion"],
            RetryCount=json_dct["RetryCount"],
            DownloadDate=json_dct["DownloadDate"],
            DailyDownload=json_dct["DailyDownload"],
            StartHour=json_dct["StartHour"],
            EndHour=json_dct["EndHour"],
            StartDownloadOnProgramStartup=json_dct["StartDownloadOnProgramStartup"],
            DownloadSpeed=json_dct["DownloadSpeed"],
            CloseProgramAfterDownload=json_dct["CloseProgramAfterDownload"],
            ShutDownSystemAfterDownloads=json_dct["ShutDownSystemAfterDownloads"],
            CreatedOnUtc=json_dct["CreatedOnUtc"]
        )

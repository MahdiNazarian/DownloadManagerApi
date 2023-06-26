import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import DATETIME2, UNIQUEIDENTIFIER, NVARCHAR
import datetime
from DbContext.DbContext import Base


class DbDownloadLine(Base):
    __tablename__ = "DbDownloadLine"
    Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    GuId = Column(UNIQUEIDENTIFIER, nullable=False, default=uuid.uuid4)
    Deleted = Column(Boolean, default=False, nullable=False)
    UserId = Column(BigInteger, ForeignKey("DbUser.Id"), nullable=False)
    TimingId = Column(BigInteger, ForeignKey("DbTiming.Id"), nullable=False)
    DownloadLineName = Column(NVARCHAR, default="", nullable=False)
    CreatedOnUtc = Column(DATETIME2, default=datetime.datetime.now(), nullable=False)
    Timing = relationship("DbTiming")
    User = relationship("DbUser")

    @staticmethod
    def from_json_update(json_dct):
        return DbDownloadLine(
            Id=json_dct["Id"] if json_dct["Id"] is not None else None if json_dct["Id"] != 0 else None,
            GuId=uuid.UUID(json_dct["GuId"]) if json_dct["GuId"] is not None else None if json_dct["GuId"] != "" else None,
            Deleted=json_dct["Deleted"],
            UserId=json_dct["UserId"],
            TimingId=json_dct["TimingId"],
            DownloadLineName=json_dct["DownloadLineName"],
            CreatedOnUtc=json_dct["CreatedOnUtc"]
        )

    @staticmethod
    def from_json_insert(json_dct):
        return DbDownloadLine(
            UserId=json_dct["UserId"],
            TimingId=json_dct["TimingId"],
            DownloadLineName=json_dct["DownloadLineName"],
            CreatedOnUtc=json_dct["CreatedOnUtc"]
        )

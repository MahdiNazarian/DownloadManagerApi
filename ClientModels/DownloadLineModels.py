import datetime

from pydantic import BaseModel


class DownloadLineInsertModel(BaseModel):
    UserId: int
    TimingId: int
    DownloadLineName: str
    CreatedOnUtc: datetime.datetime


class DownloadLineUpdateModel(DownloadLineInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

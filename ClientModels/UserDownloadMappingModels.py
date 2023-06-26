import datetime

from pydantic import BaseModel


class UserDownloadMappingInsertModel(BaseModel):
    UserId: int
    DownloadFileId: int
    DownloadStartDate: datetime.datetime
    DownloadEndDate: datetime.datetime


class UserDownloadMappingUpdateModel(UserDownloadMappingInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

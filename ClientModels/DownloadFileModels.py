import datetime

from pydantic import BaseModel


class DownloadFileInsertModel(BaseModel):
    DownloadLineId: int
    FileName: str
    FileSize: int
    DownloadPath: str
    DownloadStatus: str
    RemainingTime: int
    DownloadedSize: int
    HasSpeedLimit: bool
    DownloadSpeed: int
    Description: str


class DownloadFileUpdateModel(DownloadFileInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

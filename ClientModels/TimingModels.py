import datetime

from pydantic import BaseModel


class TimingInsertModel(BaseModel):
    UserId: int
    SpeedLimited: bool
    DisconnectAfterCompletion: bool
    RetryCount: int
    DownloadDate: datetime.datetime
    DailyDownload: bool
    StartHour: str
    EndHour: str
    StartDownloadOnProgramStartup: bool
    DownloadSpeed: int
    CloseProgramAfterDownload: bool
    ShutDownSystemAfterDownloads: bool


class TimingUpdateModel(TimingInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

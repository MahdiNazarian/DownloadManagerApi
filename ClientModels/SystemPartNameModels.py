import datetime

from pydantic import BaseModel


class SystemPartNameInsertModel(BaseModel):
    Title: str
    SystemPartName: str
    Url: str


class SystemPartNameUpdateModel(SystemPartNameInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

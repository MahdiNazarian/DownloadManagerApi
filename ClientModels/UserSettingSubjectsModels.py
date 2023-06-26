import datetime

from pydantic import BaseModel


class UserSettingSubjectsInsertModel(BaseModel):
    SubjectName: str


class UserSettingSubjectsUpdateModel(UserSettingSubjectsInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

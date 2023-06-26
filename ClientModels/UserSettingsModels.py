import datetime

from pydantic import BaseModel


class UserSettingsInsertModel(BaseModel):
    UserId: int
    UserSettingSubjectId: int
    SettingName: str
    SettingValue: str
    SettingDesc: str


class UserSettingsUpdateModel(UserSettingsInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

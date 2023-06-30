import datetime

from pydantic import BaseModel


class SettingsInsertModel(BaseModel):
    SettingName: str
    SettingValue: str
    SettingDesc: str


class SettingsUpdateModel(SettingsInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

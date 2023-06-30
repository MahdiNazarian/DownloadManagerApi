import datetime

from pydantic import BaseModel


class UserSystemPartNameMappingInsertModel(BaseModel):
    UserId: int
    SystemPartNameId: int


class UserSystemPartNameMappingUpdateModel(UserSystemPartNameMappingInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

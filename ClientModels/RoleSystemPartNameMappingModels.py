import datetime

from pydantic import BaseModel


class SystemPartNameMappingInsertModel(BaseModel):
    RoleId: int
    SystemPartNameId: int


class SystemPartNameMappingUpdateModel(SystemPartNameMappingInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

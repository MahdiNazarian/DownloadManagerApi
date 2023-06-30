import datetime

from pydantic import BaseModel


class UserRoleMappingInsertModel(BaseModel):
    UserId: int
    RoleId: int


class UserRoleMappingUpdateModel(UserRoleMappingInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

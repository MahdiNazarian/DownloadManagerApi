import datetime

from pydantic import BaseModel


class RoleInsertModel(BaseModel):
    Type: str
    Name: str


class RoleUpdateModel(RoleInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None

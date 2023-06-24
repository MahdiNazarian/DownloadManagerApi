import datetime

from pydantic import BaseModel


class UserInsertModel(BaseModel):
    Email: str
    FirstName: str
    LastName: str
    IsEmailConfirmed: bool
    PhoneNumber: str
    IsPhoneNumberConfirmed: bool
    Password: str


class UserUpdateModel(UserInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None
    LastLogin: datetime.datetime | None = None

import datetime

from pydantic import BaseModel


class UserInsertAndUpdateModel(BaseModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None
    Email: str
    FirstName: str
    LastName: str
    IsEmailConfirmed: bool
    PhoneNumber: str
    IsPhoneNumberConfirmed: bool
    Password: str
    LastLogin: datetime.datetime | None = None
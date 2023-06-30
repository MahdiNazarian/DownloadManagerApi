import datetime

from pydantic import BaseModel


class UserRegisterModel(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    PhonNumber: str
    Password: str
    Re_Password: str

import datetime

from pydantic import BaseModel


class UserRegisterModel(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    PhonNumber: str
    Password: str
    Re_Password: str


class UserLoginModel(BaseModel):
    EmailOrPhoneNumber: str
    Password: str
    remember_me: bool

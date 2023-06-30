from typing import Annotated

from fastapi import Depends

from BussinessLogic.BaseBll import BaseBll
from Repositories.UserRepository import UserRepository


class UserBll(BaseBll):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(repository=self.repository)

    def get_user_by_email_phone_number(self, email_phone_number: str):
        return self.repository.get_user_by_email_phone_number(email_phone_number)

from typing import Annotated

from fastapi import Depends

from BussinessLogic.BaseBll import BaseBll
from Repositories.UserRepository import UserRepository


class UserBll(BaseBll):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(repository=self.repository)


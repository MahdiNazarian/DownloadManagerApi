from BussinessLogic.BaseBll import BaseBll
from Repositories.UserLoginsRepository import UserLoginsRepository


class UserLoginsBll(BaseBll):
    def __init__(self):
        self.repository = UserLoginsRepository()
        super().__init__(repository=self.repository)


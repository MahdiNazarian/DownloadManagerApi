from BussinessLogic.BaseBll import BaseBll
from Repositories.UserLoginsRepository import UserLoginsRepository


class UserLoginsBll(BaseBll):
    def __init__(self):
        self.repository = UserLoginsRepository()
        super().__init__(repository=self.repository)

    def get_user_login_attempts_by_user_id_desc(self, user_id: int):
        self.repository.get_user_login_attempts_by_user_id_desc(user_id)

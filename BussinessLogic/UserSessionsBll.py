from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSessionsRepository import UserSessionsRepository


class UserSessionsBll(BaseBll):
    def __init__(self):
        self.repository = UserSessionsRepository()
        super().__init__(repository=self.repository)

    def get_user_sessions_by_user_id(self, user_id: int):
        return self.repository.get_user_sessions_by_user_id(user_id)

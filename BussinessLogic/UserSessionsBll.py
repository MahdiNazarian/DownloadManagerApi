from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSessionsRepository import UserSessionsRepository


class UserSessionsBll(BaseBll):
    def __init__(self):
        self.repository = UserSessionsRepository()
        super().__init__(repository=self.repository)


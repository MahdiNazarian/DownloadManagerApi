from BussinessLogic.BaseBll import BaseBll
from Repositories.UserRoleMappingRepository import UserRoleMappingRepository


class UserRoleMappingBll(BaseBll):
    def __init__(self):
        self.repository = UserRoleMappingRepository()
        super().__init__(repository=self.repository)


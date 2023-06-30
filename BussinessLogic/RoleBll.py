from BussinessLogic.BaseBll import BaseBll
from Repositories.RoleRepository import RoleRepository


class RoleBll(BaseBll):
    def __init__(self):
        self.repository = RoleRepository()
        super().__init__(repository=self.repository)


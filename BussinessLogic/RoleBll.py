from BussinessLogic.BaseBll import BaseBll
from Repositories.RoleRepository import RoleRepository


class RoleBll(BaseBll):
    def __init__(self):
        self.repository = RoleRepository()
        super().__init__(repository=self.repository)

    def get_role_by_name(self, role_name: str):
        return self.repository.get_role_by_name(role_name)

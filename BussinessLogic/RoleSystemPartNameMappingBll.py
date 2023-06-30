from BussinessLogic.BaseBll import BaseBll
from Repositories.RoleSystemPartNameRepository import RoleSystemPartNameRepository


class RoleSystemPartNameMappingBll(BaseBll):
    def __init__(self):
        self.repository = RoleSystemPartNameRepository()
        super().__init__(repository=self.repository)


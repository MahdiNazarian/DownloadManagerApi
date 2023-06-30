from BussinessLogic.BaseBll import BaseBll
from Repositories.RoleSystemPartNameRepository import RoleSystemPartNameRepository


class RoleSystemPartNameMappingBll(BaseBll):
    def __init__(self):
        self.repository = RoleSystemPartNameRepository()
        super().__init__(repository=self.repository)

    def get_role_system_part_name_mapping_by_role_id(self, role_id: int):
        return self.repository.get_role_system_part_name_mapping_by_role_id(role_id)

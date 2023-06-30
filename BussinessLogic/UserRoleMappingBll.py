from BussinessLogic.BaseBll import BaseBll
from Models.DbUserRoleMapping import DbUserRoleMapping
from Repositories.UserRoleMappingRepository import UserRoleMappingRepository


class UserRoleMappingBll(BaseBll):
    def __init__(self):
        self.repository = UserRoleMappingRepository()
        super().__init__(repository=self.repository)

    def get_user_role_mapping_by_user_id(self, user_id: int):
        return self.repository.get_user_role_mapping_by_user_id(user_id)

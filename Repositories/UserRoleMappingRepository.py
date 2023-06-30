from Repositories import BaseRepository
from Models import DbUserRoleMapping


class UserRoleMappingRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserRoleMapping.DbUserRoleMapping)


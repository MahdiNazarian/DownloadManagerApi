from Repositories import BaseRepository
from Models import DbRoleSystemPartNameMapping


class RoleSystemPartNameRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbRoleSystemPartNameMapping.DbRoleSystemPartNameMapping)


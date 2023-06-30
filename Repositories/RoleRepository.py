from Repositories import BaseRepository
from Models import DbRole


class RoleRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbRole.DbRole)


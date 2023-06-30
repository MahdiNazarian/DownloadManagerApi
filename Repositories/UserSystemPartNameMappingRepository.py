from Repositories import BaseRepository
from Models import DbUserSystemPartNameMapping


class UserSystemPartNameMappingRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserSystemPartNameMapping.DbUserSystemPartNameMapping)


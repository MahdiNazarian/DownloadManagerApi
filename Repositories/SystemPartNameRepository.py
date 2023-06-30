from Repositories import BaseRepository
from Models import DbSystemPartName


class SystemPartNameRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbSystemPartName.DbSystemPartName)


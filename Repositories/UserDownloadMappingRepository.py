from Repositories import BaseRepository
from Models import DbUserDownloadMapping


class UserDownloadMappingRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserDownloadMapping.DbUserDownloadMapping)


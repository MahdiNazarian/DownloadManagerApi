from Repositories import BaseRepository
from Models import DbDownloadLine


class DownloadLineRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbDownloadLine.DbDownloadLine)


from Repositories import BaseRepository
from Models import DbDownloadFile


class DownloadFileRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbDownloadFile.DbDownloadFile)


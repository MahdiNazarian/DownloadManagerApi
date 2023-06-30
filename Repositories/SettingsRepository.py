from Repositories import BaseRepository
from Models import DbSettings


class SettingsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbSettings.DbSettings)


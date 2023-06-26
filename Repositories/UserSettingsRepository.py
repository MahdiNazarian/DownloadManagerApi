from Repositories import BaseRepository
from Models import DbUserSettings


class UserSettingsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserSettings.DbUserSettings)


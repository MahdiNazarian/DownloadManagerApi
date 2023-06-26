from Repositories import BaseRepository
from Models import DbUserSettingSubjects


class UserSettingSubjectRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserSettingSubjects.DbUserSettingSubjects)


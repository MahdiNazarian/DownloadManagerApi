from Repositories import BaseRepository
from Models import DbUserSessions


class UserSessionsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserSessions.DbUserSessions)


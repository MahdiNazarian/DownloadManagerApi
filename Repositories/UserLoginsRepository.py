from Repositories import BaseRepository
from Models import DbUserLogins


class UserLoginsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserLogins.DbUserLogins)


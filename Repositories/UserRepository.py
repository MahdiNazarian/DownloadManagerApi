from Repositories import BaseRepository
from Models import DbUser


class UserRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUser.DbUser)

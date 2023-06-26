from Repositories import BaseRepository
from Models import DbTiming


class TimingRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbTiming.DbTiming)


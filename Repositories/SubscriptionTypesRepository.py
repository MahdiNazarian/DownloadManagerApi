from Repositories import BaseRepository
from Models import DbSubscriptionTypes


class SubscriptionTypesRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbSubscriptionTypes.DbSubscriptionTypes)

from Repositories import BaseRepository
from Models import DbUserSubscription


class UserSubscriptionRepository(BaseRepository.BaseRepository):
    def __init__(self):
        super().__init__(DbUserSubscription.DbUserSubscriptions)

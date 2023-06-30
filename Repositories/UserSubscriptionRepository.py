import datetime

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbUserSubscription


class UserSubscriptionRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbUserSubscription.DbUserSubscriptions)

    def get_user_active_subs_by_user_id(self, user_id: int):
        return self.db.query(DbUserSubscription.DbUserSubscriptions).filter(
            and_(
                DbUserSubscription.DbUserSubscriptions.UserId == user_id,
                DbUserSubscription.DbUserSubscriptions.SubscriptionEndDate > datetime.datetime.now()
            )
        ).all()

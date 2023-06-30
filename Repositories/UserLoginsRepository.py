import datetime

from sqlalchemy.orm import Session
from sqlalchemy import and_, desc

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbUserLogins


class UserLoginsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbUserLogins.DbUserLogins)

    def get_user_login_attempts_by_user_id_desc(self, user_id: int):
        return self.db.query(DbUserLogins.DbUserLogins).filter(
            and_(
                DbUserLogins.DbUserLogins.UserId == user_id,
                DbUserLogins.DbUserLogins.LoginAttemptTime > (datetime.datetime.now() - datetime.timedelta(hours=24))
            )
        ).order_by(desc(DbUserLogins.DbUserLogins.LoginAttemptTime)).all()

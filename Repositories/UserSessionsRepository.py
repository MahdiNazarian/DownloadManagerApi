from sqlalchemy.orm import Session
from sqlalchemy import desc

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbUserSessions


class UserSessionsRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbUserSessions.DbUserSessions)

    def get_user_sessions_by_user_id(self, user_id: int):
        return self.db.query(DbUserSessions.DbUserSessions).filter(DbUserSessions.DbUserSessions.UserId == user_id).order_by(desc(DbUserSessions.DbUserSessions.CreatedOnUtc)).first()


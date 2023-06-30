from sqlalchemy.orm import Session
from sqlalchemy import or_

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbUser


class UserRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbUser.DbUser)

    def __call__(self, *args, **kwargs):
        pass

    def get_user_by_email_phone_number(self, email_phone_number: str):
        return self.db.query(DbUser.DbUser).filter(or_(DbUser.DbUser.Email == email_phone_number, DbUser.DbUser.PhoneNumber == email_phone_number)).first()

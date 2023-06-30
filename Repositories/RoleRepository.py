from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbRole
from sqlalchemy.orm import Session


class RoleRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbRole.DbRole)

    def get_role_by_name(self, role_name: str):
        return self.db.query(DbRole.DbRole).filter(DbRole.DbRole.Name == role_name).first()

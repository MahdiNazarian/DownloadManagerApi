from sqlalchemy.orm import Session

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbUserRoleMapping


class UserRoleMappingRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbUserRoleMapping.DbUserRoleMapping)

    def get_user_role_mapping_by_user_id(self, user_id: int):
        return self.db.query(DbUserRoleMapping.DbUserRoleMapping).filter(DbUserRoleMapping.DbUserRoleMapping.UserId == user_id).all()


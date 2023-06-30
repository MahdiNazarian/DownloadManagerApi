from sqlalchemy.orm import Session

from DbContext.DbContext import get_db
from Repositories import BaseRepository
from Models import DbRoleSystemPartNameMapping


class RoleSystemPartNameRepository(BaseRepository.BaseRepository):
    def __init__(self):
        self.db: Session = next(get_db())
        super().__init__(DbRoleSystemPartNameMapping.DbRoleSystemPartNameMapping)

    def get_role_system_part_name_mapping_by_role_id(self, role_id: int):
        return self.db.query(DbRoleSystemPartNameMapping.DbRoleSystemPartNameMapping).filter(DbRoleSystemPartNameMapping.DbRoleSystemPartNameMapping.RoleId == role_id).all()

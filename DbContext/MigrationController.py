from DbContext.DbContext import engine
from Models import DbUser


class MigrationController:
    def start_migrate(self):
        DbUser.Base.metadata.create_all(bind=engine)

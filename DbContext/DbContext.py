from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "Server=LAPTOP-4L8IOKSN\\MSSQLSERVER2;Database=Download_Manager_DB;Trusted_Connection=True;MultipleActiveResultSets=True;"
SQLALCHEMY_DATABASE_URL = URL.create(
    "mssql+pyodbc",
    host="LAPTOP-4L8IOKSN\\MSSQLSERVER2",
    database="Download_Manager_DB",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
        "authentication": "ActiveDirectoryIntegrated",
    },
)
# SQLALCHEMY_DATABASE_URL = "Server=;Database=;User ID=;Password=;Trusted_Connection=False;"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

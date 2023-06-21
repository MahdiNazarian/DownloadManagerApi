from sqlalchemy.orm import Session
from sqlalchemy import BigInteger, Update
from fastapi import Depends
from DbContext.DbContext import get_db
from Models.DbBaseModel import DbBaseModel
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER


class BaseRepository:
    def __init__(self, model):
        self.db: Session = Depends(get_db())
        self.model = model

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_guid(self, guid: UNIQUEIDENTIFIER):
        return self.db.query(self.model).filter(self.model.GuId == guid).first()

    def get_by_id(self, user_id: BigInteger):
        return self.db.query(self.model).filter(self.model.Id == user_id).first()

    def insert_data(self, data):
        insert_data = data
        self.db.add(insert_data)
        self.db.commit()
        self.db.refresh(insert_data)
        return insert_data

    def insert_range_data(self, data_list):
        insert_data_list = data_list
        self.db.add_all(insert_data_list)
        self.db.commit()
        self.db.refresh(insert_data_list)
        return insert_data_list

    def update_data(self, data):
        update_data = data
        self.db.execute(Update(self.model), data)

import uuid

from sqlalchemy.orm import Session
from sqlalchemy import BigInteger, Update
from fastapi import Depends
from DbContext.DbContext import get_db
from Models.DbBaseModel import DbBaseModel
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER


class BaseRepository:
    def __init__(self, model):
        self.db: Session = next(get_db())
        self.model = model

    def get_all(self):
        return self.db.query(self.model).filter(self.model.Deleted != True).all()

    def get_by_guid(self, guid: uuid.UUID):
        return self.db.query(self.model).filter(self.model.GuId == guid, self.model.Deleted != True).first()

    def get_by_id(self, row_id: BigInteger):
        return self.db.query(self.model).filter(self.model.Id == row_id, self.model.Deleted != True).first()

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
        if type(insert_data_list) is list:
            for d in insert_data_list:
                self.db.refresh(d)
        else:
            self.db.refresh(insert_data_list)
        return insert_data_list

    def update_data(self, data):
        update_data = data
        item = self.db.query(self.model).filter(self.model.Id == update_data.Id).first()
        for attr, value in update_data.__dict__.items():
            if attr == "_sa_instance_state" or attr == "Id" or attr == "GuId" or attr == "Deleted":
                continue
            if value is None or value == "" or value == 0:
                continue
            setattr(item, attr, value)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update_list_data(self, data_list):
        update_data = data_list
        selected_data = []
        for i, update_data_item in enumerate(update_data):
            item = self.db.query(self.model).filter(self.model.Id == update_data_item.Id).first()
            for attr, value in update_data_item.__dict__.items():
                if attr == "_sa_instance_state" or attr == "Id" or attr == "GuId" or attr == "Deleted":
                    continue
                if value is None or value == "" or value == 0:
                    continue
                setattr(item, attr, value)
            self.db.commit()
            self.db.refresh(item)
            selected_data.append(item)
        return selected_data

    def delete_data(self, data):
        delete_data = self.db.query(self.model).filter(self.model.Id == data.Id).first()
        delete_data.Deleted = True
        self.db.commit()
        self.db.refresh(delete_data)
        return delete_data

    def delete_by_id(self, row_id: BigInteger):
        delete_data = self.db.query(self.model).filter(self.model.Id == row_id).first()
        delete_data.Deleted = True
        self.db.commit()
        self.db.refresh(delete_data)
        return delete_data

    def delete_by_guid(self, guid: uuid.UUID):
        delete_data = self.db.query(self.model).filter(self.model.GuId == guid).first()
        delete_data.Deleted = True
        self.db.commit()
        self.db.refresh(delete_data)
        return delete_data

    def get_page_by_page(self, page_number, page_row_count):
        return self.db.query(self.model).filter(self.model.Deleted != True).order_by(self.model.Id).offset((page_number-1)*page_row_count).limit(page_row_count).all()

    def get_from_to(self, start_index, count):
        return self.db.query(self.model).filter(self.model.Deleted != True).order_by(self.model.Id).offset(start_index).limit(count).all()

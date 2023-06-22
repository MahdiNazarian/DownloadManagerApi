from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy import BigInteger


class BaseBll:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_guid(self, guid: UNIQUEIDENTIFIER):
        return self.repository.get_by_guid(guid=guid)

    def get_by_id(self, row_id: BigInteger):
        return self.repository.get_by_id(row_id=row_id)

    def insert_data(self, data):
        return self.repository.insert_data(data=data)

    def insert_range_data(self, data_list):
        return self.repository.insert_range_data(data_list=data_list)

    def update_data(self, data):
        return self.repository.update_data(data=data)

    def delete_data(self, data):
        return self.repository.delete_data(data=data)

    def delete_by_id(self, row_id: BigInteger):
        return self.repository.delete_by_id(row_id=row_id)

    def delete_by_guid(self, guid: UNIQUEIDENTIFIER):
        return self.repository.delete_by_guid(guid=guid)

    def get_page_by_page(self, page_number, page_row_count):
        return self.repository.get_page_by_page(page_number=page_number, page_row_count=page_row_count)

    def get_from_to(self, start_index, count):
        return self.repository.get_from_to(start_index=start_index, count=count)

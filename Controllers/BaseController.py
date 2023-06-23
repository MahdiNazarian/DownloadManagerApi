from fastapi import APIRouter, HTTPException
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy import BigInteger

from ClientModels.ResponseModel import ResponseModel

base_router: APIRouter


class BaseController:
    def __init__(self, bll, router: APIRouter):
        self.bll = bll
        self.router: APIRouter = router
        globals.base_router = self.router

    @base_router.get("/get_all")
    def get_all(self):
        get_result = self.bll.get_all()
        if get_result is not None:
            return ResponseModel(status=200, message="Data Sent", data=get_result)
        else:
            raise HTTPException(status_code=404, detail="No Data Found")

    @base_router.get("/get_by_guid/{guid}")
    def get_by_guid(self, guid: UNIQUEIDENTIFIER):
        if guid is not None:
            get_result = self.bll.get_by_guid(guid=guid)
            if get_result is not None:
                return ResponseModel(status=200, message="Data Sent", data=get_result)
            else:
                raise HTTPException(status_code=404, detail="No Data Found")
        else:
            raise HTTPException(status_code=400, detail="No guid entered")

    @base_router.get("/get_by_id/{row_id}")
    def get_by_id(self, row_id: BigInteger):
        if row_id is not None:
            get_result = self.bll.get_by_id(row_id=row_id)
            if get_result is not None:
                return ResponseModel(status=200, message="Data Sent", data=get_result)
            else:
                raise HTTPException(status_code=404, detail="No Data Found")
        else:
            raise HTTPException(status_code=400, detail="No row_id entered")

    @base_router.post("/add")
    def insert_data(self, data):
        if data is not None:
            insert_result = self.bll.insert_data(data=data)
            if insert_result is not None:
                return ResponseModel(status=200, message="Row Inserted", data=insert_result)
            else:
                raise HTTPException(status_code=500, detail="Insert Failed")
        else:
            raise HTTPException(status_code=400, detail="No data entered")

    @base_router.post("/add_all")
    def insert_range_data(self, data_list):
        if data_list is not None:
            insert_result = self.bll.insert_range_data(data_list=data_list)
            if insert_result is not None:
                return ResponseModel(status=200, message="Rows Inserted", data=insert_result)
            else:
                raise HTTPException(status_code=500, detail="Insert Failed")
        else:
            raise HTTPException(status_code=400, detail="No data_list entered")

    @base_router.put("/update")
    def update_data(self, data):
        if data is not None:
            update_result = self.bll.update_data(data=data)
            if update_result is not None:
                return ResponseModel(status=200, message="data Updated Successfully", data=update_result)
            else:
                raise HTTPException(status_code=500, detail="Update Failed")
        else:
            raise HTTPException(status_code=400, detail="No data entered")

    @base_router.delete("/delete")
    def delete_data(self, data):
        if data is not None:
            delete_result = self.bll.delete_data(data=data)
            if delete_result is not None:
                return ResponseModel(status=200, message="data deleted Successfully", data=delete_result)
            else:
                raise HTTPException(status_code=500, detail="delete Failed")
        else:
            raise HTTPException(status_code=400, detail="No data entered")

    @base_router.delete("/delete_by_id/{row_id}")
    def delete_by_id(self, row_id: BigInteger):
        if row_id is not None:
            delete_result = self.bll.delete_by_id(row_id=row_id)
            if delete_result is not None:
                return ResponseModel(status=200, message="data deleted Successfully", data=delete_result)
            else:
                raise HTTPException(status_code=500, detail="delete Failed")
        else:
            raise HTTPException(status_code=400, detail="No row id entered")

    @base_router.delete("/delete_by_guid/{guid}")
    def delete_by_guid(self, guid: UNIQUEIDENTIFIER):
        if guid is not None:
            delete_result = self.bll.delete_by_guid(guid=guid)
            if delete_result is not None:
                return ResponseModel(status=200, message="data deleted Successfully", data=delete_result)
            else:
                raise HTTPException(status_code=500, detail="delete Failed")
        else:
            raise HTTPException(status_code=400, detail="No guid entered")

    @base_router.get("/get_page_by_page")
    def get_page_by_page(self, page_number: int, page_row_count: int):
        if page_number is not None and page_row_count is not None:
            get_result = self.bll.get_page_by_page(page_number=page_number, page_row_count=page_row_count)
            if get_result is not None:
                return ResponseModel(status=200, message="Data Sent", data=get_result)
            else:
                raise HTTPException(status_code=404, detail="No Data Found")
        else:
            raise HTTPException(status_code=400, detail="No page number or page row count entered")

    @base_router.get("/get_from_to")
    def get_from_to(self, start_index: int, count: int):
        if start_index is not None and count is not None:
            get_result = self.bll.get_from_to(start_index=start_index, count=count)
            if get_result is not None:
                return ResponseModel(status=200, message="Data Sent", data=get_result)
            else:
                raise HTTPException(status_code=404, detail="No Data Found")
        else:
            raise HTTPException(status_code=400, detail="No start index or page count entered")

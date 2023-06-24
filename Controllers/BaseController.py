import json
import uuid

from fastapi import APIRouter, HTTPException
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy import BigInteger

from ClientModels.ResponseModel import ResponseModel


class BaseController:
    def __init__(self, bll, router: APIRouter, db_model_instance, insert_model, update_model, delete_model):
        self.bll = bll
        self.router: APIRouter = router
        base_router = self.router
        self.db_model_instance = db_model_instance
        self.insert_model = insert_model
        self.update_model = update_model
        self.delete_model = delete_model

        @base_router.get("/get_all")
        def get_all():
            get_result = self.bll.get_all()
            if get_result is not None:
                return ResponseModel(status_code=200, message="Data Sent", data=get_result)
            else:
                raise HTTPException(status_code=404, detail="No Data Found")

        @base_router.get("/get_by_guid/{guid}")
        def get_by_guid(guid: str):
            if guid is not None:
                converted_guid = uuid.UUID(guid)
                get_result = self.bll.get_by_guid(guid=converted_guid)
                if get_result is not None:
                    return ResponseModel(status_code=200, message="Data Sent", data=get_result)
                else:
                    raise HTTPException(status_code=404, detail="No Data Found")
            else:
                raise HTTPException(status_code=400, detail="No guid entered")

        @base_router.get("/get_by_id/{row_id}")
        def get_by_id(row_id: int):
            if row_id is not None:
                get_result = self.bll.get_by_id(row_id=row_id)
                if get_result is not None:
                    return ResponseModel(status_code=200, message="Data Sent", data=get_result)
                else:
                    raise HTTPException(status_code=404, detail="No Data Found")
            else:
                raise HTTPException(status_code=400, detail="No row_id entered")

        @base_router.post("/add")
        def insert_data(data: insert_model):
            if data is not None:
                db_insert_data = db_model_instance.from_json_insert(json.loads(data.json()))
                insert_result = self.bll.insert_data(data=db_insert_data)
                if insert_result is not None:
                    return ResponseModel(status_code=200, message="Row Inserted", data=insert_result)
                else:
                    raise HTTPException(status_code=500, detail="Insert Failed")
            else:
                raise HTTPException(status_code=400, detail="No data entered")

        @base_router.post("/add_all")
        def insert_range_data(data_list: list[insert_model]):
            if data_list is not None:
                db_range_insert_data = [db_model_instance.from_json_insert(json.loads(d.json())) for d in data_list]
                insert_result = self.bll.insert_range_data(data_list=db_range_insert_data)
                if insert_result is not None:
                    return ResponseModel(status_code=200, message="Rows Inserted", data=insert_result)
                else:
                    raise HTTPException(status_code=500, detail="Insert Failed")
            else:
                raise HTTPException(status_code=400, detail="No data_list entered")

        @base_router.put("/update")
        def update_data(data: update_model):
            if data is not None:
                db_update_data = db_model_instance.from_json_update(json.loads(data.json()))
                update_result = self.bll.update_data(data=db_update_data)
                if update_result is not None:
                    return ResponseModel(status_code=200, message="data Updated Successfully", data=update_result)
                else:
                    raise HTTPException(status_code=500, detail="Update Failed")
            else:
                raise HTTPException(status_code=400, detail="No data entered")

        @base_router.put("/update_all")
        def update_list_data(data_list: list[update_model]):
            if data_list is not None:
                db_update_data = [db_model_instance.from_json_update(json.loads(d.json())) for d in data_list]
                update_result = self.bll.update_list_data(data_list=db_update_data)
                if update_result is not None:
                    return ResponseModel(status_code=200, message="data Updated Successfully", data=update_result)
                else:
                    raise HTTPException(status_code=500, detail="Update Failed")
            else:
                raise HTTPException(status_code=400, detail="No data entered")

        @base_router.delete("/delete")
        def delete_data(data: delete_model):
            if data is not None:
                db_delete_data = db_model_instance.from_json_update(json.loads(data.json()))
                delete_result = self.bll.delete_data(data=db_delete_data)
                if delete_result is not None:
                    return ResponseModel(status_code=200, message="data deleted Successfully", data=delete_result)
                else:
                    raise HTTPException(status_code=500, detail="delete Failed")
            else:
                raise HTTPException(status_code=400, detail="No data entered")

        @base_router.delete("/delete_by_id/{row_id}")
        def delete_by_id(row_id: int):
            if row_id is not None:
                delete_result = self.bll.delete_by_id(row_id=row_id)
                if delete_result is not None:
                    return ResponseModel(status_code=200, message="data deleted Successfully", data=delete_result)
                else:
                    raise HTTPException(status_code=500, detail="delete Failed")
            else:
                raise HTTPException(status_code=400, detail="No row id entered")

        @base_router.delete("/delete_by_guid/{guid}")
        def delete_by_guid(guid: str):
            if guid is not None:
                delete_result = self.bll.delete_by_guid(guid=guid)
                if delete_result is not None:
                    return ResponseModel(status_code=200, message="data deleted Successfully", data=delete_result)
                else:
                    raise HTTPException(status_code=500, detail="delete Failed")
            else:
                raise HTTPException(status_code=400, detail="No guid entered")

        @base_router.get("/get_page_by_page")
        def get_page_by_page(page_number: int, page_row_count: int):
            if page_number is not None and page_row_count is not None:
                get_result = self.bll.get_page_by_page(page_number=page_number, page_row_count=page_row_count)
                if get_result is not None:
                    return ResponseModel(status_code=200, message="Data Sent", data=get_result)
                else:
                    raise HTTPException(status_code=404, detail="No Data Found")
            else:
                raise HTTPException(status_code=400, detail="No page number or page row count entered")

        @base_router.get("/get_from_to")
        def get_from_to(start_index: int, count: int):
            if start_index is not None and count is not None:
                get_result = self.bll.get_from_to(start_index=start_index, count=count)
                if get_result is not None:
                    return ResponseModel(status_code=200, message="Data Sent", data=get_result)
                else:
                    raise HTTPException(status_code=404, detail="No Data Found")
            else:
                raise HTTPException(status_code=400, detail="No start index or page count entered")

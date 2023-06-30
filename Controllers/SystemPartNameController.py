import ClientModels.SystemPartNameModels
from Controllers.BaseController import BaseController
from BussinessLogic.SystemPartNameBll import SystemPartNameBll
from fastapi import Depends, APIRouter

from Models.DbSystemPartName import DbSystemPartName


class SystemPartNameController(BaseController):
    def __init__(self):
        self.bll = SystemPartNameBll()
        self.router: APIRouter = APIRouter(
            prefix="/system_part_name",
            tags=["system_part_name"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbSystemPartName()
        self.insert_model = ClientModels.SystemPartNameModels.SystemPartNameInsertModel
        self.update_model = ClientModels.SystemPartNameModels.SystemPartNameUpdateModel
        self.delete_model = ClientModels.SystemPartNameModels.SystemPartNameUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
